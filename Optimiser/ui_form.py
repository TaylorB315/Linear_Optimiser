# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(718, 639)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 651, 626))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.barUnusableInput = QLineEdit(self.verticalLayoutWidget)
        self.barUnusableInput.setObjectName(u"barUnusableInput")
        self.barUnusableInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.barUnusableInput, 4, 1, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 6, 0, 1, 1)

        self.lossInput = QLineEdit(self.verticalLayoutWidget)
        self.lossInput.setObjectName(u"lossInput")
        self.lossInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.lossInput, 5, 1, 1, 1)

        self.colourInput = QLineEdit(self.verticalLayoutWidget)
        self.colourInput.setObjectName(u"colourInput")
        self.colourInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.colourInput, 1, 1, 1, 1)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line, 7, 1, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 1)

        self.cuttingEndPrepInput = QLineEdit(self.verticalLayoutWidget)
        self.cuttingEndPrepInput.setObjectName(u"cuttingEndPrepInput")
        self.cuttingEndPrepInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.cuttingEndPrepInput, 2, 1, 1, 1)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 7, 0, 1, 1)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 4, 0, 1, 1)

        self.BarSizeInput = QLineEdit(self.verticalLayoutWidget)
        self.BarSizeInput.setObjectName(u"BarSizeInput")
        self.BarSizeInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.BarSizeInput, 3, 1, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.messageInput = QLineEdit(self.verticalLayoutWidget)
        self.messageInput.setObjectName(u"messageInput")
        self.messageInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.messageInput, 6, 1, 1, 1)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 5, 0, 1, 1)

        self.PartDescInput = QLineEdit(self.verticalLayoutWidget)
        self.PartDescInput.setObjectName(u"PartDescInput")
        self.PartDescInput.setMinimumSize(QSize(350, 0))
        self.PartDescInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.PartDescInput, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.AddRowButton = QPushButton(self.verticalLayoutWidget)
        self.AddRowButton.setObjectName(u"AddRowButton")
        self.AddRowButton.setMinimumSize(QSize(100, 0))
        self.AddRowButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_9.addWidget(self.AddRowButton)

        self.RemoveRowButton = QPushButton(self.verticalLayoutWidget)
        self.RemoveRowButton.setObjectName(u"RemoveRowButton")
        self.RemoveRowButton.setMinimumSize(QSize(100, 0))
        self.RemoveRowButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_9.addWidget(self.RemoveRowButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addLayout(self.verticalLayout_9, 1, 1, 1, 1)

        self.itemsTable = QTableWidget(self.verticalLayoutWidget)
        if (self.itemsTable.columnCount() < 3):
            self.itemsTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.itemsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.itemsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.itemsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.itemsTable.rowCount() < 1):
            self.itemsTable.setRowCount(1)
        self.itemsTable.setObjectName(u"itemsTable")
        self.itemsTable.setMinimumSize(QSize(475, 0))
        self.itemsTable.setMaximumSize(QSize(475, 16777215))

        self.gridLayout_4.addWidget(self.itemsTable, 1, 0, 1, 1)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        self.label_13.setFont(font)

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.reqDateInput = QLineEdit(self.verticalLayoutWidget)
        self.reqDateInput.setObjectName(u"reqDateInput")
        self.reqDateInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.reqDateInput, 4, 1, 1, 1)

        self.operatorNameInput = QLineEdit(self.verticalLayoutWidget)
        self.operatorNameInput.setObjectName(u"operatorNameInput")
        self.operatorNameInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.operatorNameInput, 3, 1, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.invoiceNumInput = QLineEdit(self.verticalLayoutWidget)
        self.invoiceNumInput.setObjectName(u"invoiceNumInput")
        self.invoiceNumInput.setMinimumSize(QSize(350, 0))
        self.invoiceNumInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.invoiceNumInput, 0, 1, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.custNameInput = QLineEdit(self.verticalLayoutWidget)
        self.custNameInput.setObjectName(u"custNameInput")
        self.custNameInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.custNameInput, 1, 1, 1, 1)

        self.jobNameInput = QLineEdit(self.verticalLayoutWidget)
        self.jobNameInput.setObjectName(u"jobNameInput")
        self.jobNameInput.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.jobNameInput, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.line_3 = QFrame(Widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(600, 0, 3, 639))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.SubmitButton = QPushButton(Widget)
        self.SubmitButton.setObjectName(u"SubmitButton")
        self.SubmitButton.setGeometry(QRect(610, 600, 100, 29))
        self.loadButton = QPushButton(Widget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(610, 550, 100, 29))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.barUnusableInput.setText(QCoreApplication.translate("Widget", u"50", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Cutting end prep: ", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Bar size in mm: ", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Message", None))
        self.lossInput.setText(QCoreApplication.translate("Widget", u"5", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Colour/Finish: ", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"mm of bar unusable: ", None))
        self.BarSizeInput.setText(QCoreApplication.translate("Widget", u"6400", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Part Description: ", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"mm loss per cut: ", None))
        self.AddRowButton.setText(QCoreApplication.translate("Widget", u"Add row", None))
        self.RemoveRowButton.setText(QCoreApplication.translate("Widget", u"Remove row", None))
        ___qtablewidgetitem = self.itemsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Quantity", None));
        ___qtablewidgetitem1 = self.itemsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Size (mm)", None));
        ___qtablewidgetitem2 = self.itemsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Reference text", None));
        self.label_13.setText(QCoreApplication.translate("Widget", u"Items needed:", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Job/Invoice number: ", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Job/Site name: ", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Req date or message: ", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Operators name: ", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Customers name: ", None))
        self.SubmitButton.setText(QCoreApplication.translate("Widget", u"Submit", None))
        self.loadButton.setText(QCoreApplication.translate("Widget", u"Load from file", None))
    # retranslateUi

