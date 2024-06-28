# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QGridLayout, QLabel, QVBoxLayout, QFrame, QScrollArea
from PySide6.QtGui import QDoubleValidator
from PySide6.QtCore import Qt, QEvent
import pandas as pd
from collections import defaultdict

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class MainWindow(QWidget,Ui_Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.BarSizeInput.setValidator(QDoubleValidator())
        self.ui.barUnusableInput.setValidator(QDoubleValidator())
        self.ui.lossInput.setValidator(QDoubleValidator())

        self.ui.AddRowButton.clicked.connect(self.addRow)
        self.ui.RemoveRowButton.clicked.connect(self.removeRow)

        self.ui.SubmitButton.clicked.connect(self.submitInfo)

        self.ui.loadButton.clicked.connect(self.load)

        self.popup = QWidget()
        self.popup_layout = QVBoxLayout()
        self.popup.setLayout(self.popup_layout)

####Loading from a file section######################################################################################################
    def load(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            try:
                df = pd.read_excel(file_name, engine='openpyxl')
                grouped_df = self.extractParts(df)
                cutting_plans = []
                for index, row in grouped_df.iterrows():
                    description = row['Description']
                    size = row['Stock']
                    cuts = row['Cuts']
                    unusableAmount = int(self.ui.barUnusableInput.text())
                    lossAmount = int(self.ui.lossInput.text())
                    cutting_plans.append((description, self.optimize_cuts(size,unusableAmount,lossAmount,cuts)))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to read file: {e}")
            self.show_cutting_plan_popup(cutting_plans)



    def extractParts(self,df):
        required_columns = ['Description', 'Cut', 'Qty', 'Stock']
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"The required column '{column}' is not present in the file")
                return

        grouped = df.groupby(['Description', 'Stock']).apply(lambda x: list(zip(x['Qty'], x['Cut']))).reset_index()
        grouped.columns = ['Description', 'Stock', 'Cuts']

        return grouped



####Table control section######################################################################################################
    def addRow(self):
        # Get the current row count
        rowCount = self.ui.itemsTable.rowCount()
        # Insert a new row at the end
        self.ui.itemsTable.insertRow(rowCount)


    def removeRow(self):
         # Get the current row count
        rowCount = self.ui.itemsTable.rowCount()
        if rowCount > 1:
            # Remove the last row
            self.ui.itemsTable.removeRow(rowCount - 1)
        else:
            QMessageBox.warning(self, "Warning", "At least one row is needed.")

####Submitting through ui section######################################################################################################
    def submitInfo(self):
        barSize = int(self.ui.BarSizeInput.text())
        unusableAmount = int(self.ui.barUnusableInput.text())
        lossAmount = int(self.ui.lossInput.text())
        requiredCuts = self.extract_table_data()
        cuttingPlan = self.optimize_cuts(barSize, unusableAmount, lossAmount, requiredCuts)
        self.show_cutting_plan_popup([(self.ui.PartDescInput.text(), cuttingPlan)])


    def extract_table_data(self):
        required_cuts = []
        for row in range(self.ui.itemsTable.rowCount()):
            quantity_item = self.ui.itemsTable.item(row, 0)
            size_item = self.ui.itemsTable.item(row, 1)
            quantity = quantity_item.text()
            size = size_item.text()
            if quantity and size:
                required_cuts.append((int(quantity), float(size)))
        return required_cuts

####optimisation section######################################################################################################
    def optimize_cuts(self, bar_length, unusable_length, cut_loss, required_cuts):
        # Sort required cuts by size in descending order (greedy approach)
        required_cuts.sort(reverse=True, key=lambda x: x[1])

        cutting_plans = []  # Array of arrays, where each inner array represents cuts for one bar
        current_bar = []  # Cuts for the current bar
        usable_length = bar_length - unusable_length

        for quantity, size in required_cuts:
            while quantity > 0:
                if usable_length >= size:
                    current_bar.append(size)
                    usable_length -= size + cut_loss
                    quantity -= 1
                else:
                    # If current bar can't fit the size, check if the smallest cut could
                    # If it could, cut that on this bar, if not no cuts can so move on
                    quantitySmall, sizeSmall = required_cuts[len(required_cuts)-1]
                    if usable_length >= sizeSmall:
                        if quantitySmall>0:
                            current_bar.append(sizeSmall)
                            usable_length -= sizeSmall + cut_loss
                            required_cuts[len(required_cuts)-1] = (quantitySmall-1, sizeSmall)
                        else:
                            required_cuts.pop(len(required_cuts)-1)

                    else:
                        cutting_plans.append(current_bar)
                        current_bar = []
                        usable_length = bar_length - unusable_length

        # Append the last bar's cuts if there are any
        if current_bar:
            cutting_plans.append(current_bar)

        return cutting_plans

####display pop-up section######################################################################################################

    def clearPopup(self):
        # Remove all widgets from the layout
        for i in reversed(range(self.popup_layout.count())):
            widget = self.popup_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def show_cutting_plan_popup(self, cutting_plans):
        self.clearPopup()

        window = QWidget()
        window.setWindowTitle("Cutting Plan")
        grid = QGridLayout(window)
        row=0
        col=0
        for description, plan in cutting_plans:
            frame = QFrame()
            frame.setFrameShape(QFrame.Box)
            frame_layout = QVBoxLayout(frame)
            desc_label = QLabel(f"{description}:")
            frame_layout.addWidget(desc_label)

            text = ""
            for i, cuts in enumerate(plan):
                cuts_summary = self.summarize_cuts(cuts)
                text += f"Bar {i + 1}: {cuts_summary}\n"
            cut_label = QLabel(text)
            frame_layout.addWidget(cut_label)
            grid.addWidget(frame,row,col)
            col+=1
            if col>3:
                col=0
                row+=1

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(window)

        self.popup_layout.addWidget(scroll)
        self.popup.show()

    def summarize_cuts(self, cuts):
        cut_count = {}
        for cut in cuts:
            if cut in cut_count:
                cut_count[cut] += 1
            else:
                cut_count[cut] = 1
        summary = ", ".join(f"{count}x {size}" for size, count in cut_count.items())
        return summary


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
