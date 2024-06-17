# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtCore import Qt, QEvent
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

    def submitInfo(self):
        barSize = int(self.ui.BarSizeInput.text())
        unusableAmount = int(self.ui.barUnusableInput.text())
        lossAmount = int(self.ui.lossInput.text())
        requiredCuts = self.extract_table_data()
        cuttingPlan = self.optimize_cuts(barSize, unusableAmount, lossAmount, requiredCuts)
        print(cuttingPlan)


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
                        current_bar.append(sizeSmall)
                        usable_length -= sizeSmall + cut_loss
                        required_cuts[len(required_cuts)-1] = (quantitySmall-1, sizeSmall)
                    else:
                        cutting_plans.append(current_bar)
                        current_bar = []
                        usable_length = bar_length - unusable_length

        # Append the last bar's cuts if there are any
        if current_bar:
            cutting_plans.append(current_bar)

        return cutting_plans



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
