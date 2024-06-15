# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
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

        self.ui.AddRowButton.clicked.connect(self.addRow)
        self.ui.RemoveRowButton.clicked.connect(self.removeRow)

    def addRow(self):
        # Get the current row count
        rowCount = self.ui.tableWidget.rowCount()
        # Insert a new row at the end
        self.ui.tableWidget.insertRow(rowCount)


    def removeRow(self):
         # Get the current row count
        rowCount = self.ui.tableWidget.rowCount()
        if rowCount > 1:
            # Remove the last row
            self.ui.tableWidget.removeRow(rowCount - 1)
        else:
            QMessageBox.warning(self, "Warning", "At least one row is needed.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
