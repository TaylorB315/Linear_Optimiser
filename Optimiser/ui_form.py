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
        self.lineEdit_10 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_10, 4, 1, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 6, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_11, 5, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line, 7, 1, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 7, 0, 1, 1)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 4, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_9, 3, 1, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_12, 6, 1, 1, 1)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 5, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(350, 0))
        self.lineEdit_6.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 1, 1, 1)

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

        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(475, 0))
        self.tableWidget.setMaximumSize(QSize(475, 16777215))

        self.gridLayout_4.addWidget(self.tableWidget, 1, 0, 1, 1)

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

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(350, 0))
        self.lineEdit.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)

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
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 550, 100, 29))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Cutting end prep: ", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Bar size in mm: ", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Message", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Colour/Finish: ", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"mm of bar unusable: ", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Part Description: ", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"mm loss per cut: ", None))
        self.AddRowButton.setText(QCoreApplication.translate("Widget", u"Add row", None))
        self.RemoveRowButton.setText(QCoreApplication.translate("Widget", u"Remove row", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Quantity", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Size", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Reference text", None));
        self.label_13.setText(QCoreApplication.translate("Widget", u"Items needed:", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Job/Invoice number: ", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Job/Site name: ", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Req date or message: ", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Operators name: ", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Customers name: ", None))
        self.SubmitButton.setText(QCoreApplication.translate("Widget", u"Submit", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Load from file", None))
    # retranslateUi

