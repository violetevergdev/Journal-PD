# -*- coding: utf-8 -*-
from datetime import datetime

# Form implementation generated from reading ui file 'new_record2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu

from modules.gui.window.bank_list import Ui_Dialog
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from modules.optionally.delegates import TableItemDelegate



class Ui_NewRecord(object):
    def __init__(self, logger, user):
        self.logger = logger
        self.user = user
    def setFocus(self):
        self.setFocus()
    def setupUi(self, NewRecord):
        NewRecord.setObjectName("NewRecord")
        NewRecord.resize(504, 776)
        NewRecord.setStyleSheet(
'''QDialog {
	background-color: #93a5a7;
}

QLabel, QLineEdit, QPushButton, QToolButton, QDateEdit {
	font-family: Calibri;
	font-size: 20px;
}
'''        )
        self.label_new_record = QtWidgets.QLabel(NewRecord)
        self.label_new_record.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.label_new_record.setFont(font)
        self.label_new_record.setStyleSheet("color: white;\n"
"")
        self.label_new_record.setObjectName("label_new_record")
        self.main_frame = QtWidgets.QFrame(NewRecord)
        self.main_frame.setGeometry(QtCore.QRect(30, 40, 451, 711))
        self.main_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.main_frame.setStyleSheet("QFrame {\n"
"    border: 1px solid white;\n"
"    font-family: Calibri;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    font-family: Calibri;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QListView {\n"
"    background-color:white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color:white;\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.sizes_frame = QtWidgets.QFrame(self.main_frame)
        self.sizes_frame.setGeometry(QtCore.QRect(40, 420, 371, 211))
        self.sizes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sizes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sizes_frame.setObjectName("sizes_frame")
        self.widget = QtWidgets.QWidget(self.sizes_frame)
        self.widget.setGeometry(QtCore.QRect(40, 40, 301, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(45)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.size_Pens = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.size_Pens.setFont(font)
        self.size_Pens.setInputMethodHints(QtCore.Qt.ImhNone)
        self.size_Pens.setMaxLength(32767)
        self.size_Pens.setCursorPosition(0)
        self.size_Pens.setAlignment(QtCore.Qt.AlignCenter)
        self.size_Pens.setObjectName("size_Pens")
        self.horizontalLayout.addWidget(self.size_Pens)
        self.size_Pens.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.size_Pens.customContextMenuRequested.connect(lambda point: self.showContextMenu(self.size_Pens).exec_(self.size_Pens.mapToGlobal(point)))

        self.allow_Pens = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.allow_Pens.setFont(font)
        self.allow_Pens.setInputMethodHints(QtCore.Qt.ImhNone)
        self.allow_Pens.setMaxLength(32767)
        self.allow_Pens.setCursorPosition(0)
        self.allow_Pens.setAlignment(QtCore.Qt.AlignCenter)
        self.allow_Pens.setObjectName("allow_Pens")
        self.horizontalLayout.addWidget(self.allow_Pens)
        self.allow_Pens.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.allow_Pens.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.allow_Pens).exec_(self.allow_Pens.mapToGlobal(point)))

        self.widget1 = QtWidgets.QWidget(self.sizes_frame)
        self.widget1.setGeometry(QtCore.QRect(20, 10, 338, 26))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.L_sizePens = QtWidgets.QLabel(self.widget1)
        self.L_sizePens.setStyleSheet("border:none")
        self.L_sizePens.setObjectName("L_sizePens")
        self.horizontalLayout_2.addWidget(self.L_sizePens)
        self.L_allowPens = QtWidgets.QLabel(self.widget1)
        self.L_allowPens.setStyleSheet("border:none")
        self.L_allowPens.setObjectName("L_allowPens")
        self.horizontalLayout_2.addWidget(self.L_allowPens)
        self.widget2 = QtWidgets.QWidget(self.sizes_frame)
        self.widget2.setGeometry(QtCore.QRect(30, 70, 305, 26))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(45)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.L_sizeEDV = QtWidgets.QLabel(self.widget2)
        self.L_sizeEDV.setStyleSheet("border:none")
        self.L_sizeEDV.setObjectName("L_sizeEDV")
        self.horizontalLayout_3.addWidget(self.L_sizeEDV)
        self.L_allowEDV = QtWidgets.QLabel(self.widget2)
        self.L_allowEDV.setStyleSheet("border:none")
        self.L_allowEDV.setObjectName("L_allowEDV")
        self.horizontalLayout_3.addWidget(self.L_allowEDV)
        self.widget3 = QtWidgets.QWidget(self.sizes_frame)
        self.widget3.setGeometry(QtCore.QRect(40, 100, 301, 32))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(45)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.size_EDV = QtWidgets.QLineEdit(self.widget3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.size_EDV.setFont(font)
        self.size_EDV.setInputMethodHints(QtCore.Qt.ImhNone)
        self.size_EDV.setMaxLength(32767)
        self.size_EDV.setCursorPosition(0)
        self.size_EDV.setAlignment(QtCore.Qt.AlignCenter)
        self.size_EDV.setObjectName("size_EDV")
        self.horizontalLayout_4.addWidget(self.size_EDV)
        self.size_EDV.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.size_EDV.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.size_EDV).exec_(self.size_EDV.mapToGlobal(point)))

        self.allow_EDV = QtWidgets.QLineEdit(self.widget3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.allow_EDV.setFont(font)
        self.allow_EDV.setInputMethodHints(QtCore.Qt.ImhNone)
        self.allow_EDV.setMaxLength(32767)
        self.allow_EDV.setCursorPosition(0)
        self.allow_EDV.setAlignment(QtCore.Qt.AlignCenter)
        self.allow_EDV.setObjectName("allow_EDV")
        self.horizontalLayout_4.addWidget(self.allow_EDV)
        self.allow_EDV.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.allow_EDV.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.allow_EDV).exec_(self.allow_EDV.mapToGlobal(point)))

        self.widget4 = QtWidgets.QWidget(self.sizes_frame)
        self.widget4.setGeometry(QtCore.QRect(20, 130, 323, 26))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(45)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.L_sizeDMO = QtWidgets.QLabel(self.widget4)
        self.L_sizeDMO.setStyleSheet("border:none")
        self.L_sizeDMO.setObjectName("L_sizeDMO")
        self.horizontalLayout_5.addWidget(self.L_sizeDMO)
        self.L_allowDMO = QtWidgets.QLabel(self.widget4)
        self.L_allowDMO.setStyleSheet("border:none")
        self.L_allowDMO.setObjectName("L_allowDMO")
        self.horizontalLayout_5.addWidget(self.L_allowDMO)
        self.widget5 = QtWidgets.QWidget(self.sizes_frame)
        self.widget5.setGeometry(QtCore.QRect(40, 160, 301, 32))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(45)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.size_DMO = QtWidgets.QLineEdit(self.widget5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.size_DMO.setFont(font)
        self.size_DMO.setInputMethodHints(QtCore.Qt.ImhNone)
        self.size_DMO.setMaxLength(32767)
        self.size_DMO.setCursorPosition(0)
        self.size_DMO.setAlignment(QtCore.Qt.AlignCenter)
        self.size_DMO.setObjectName("size_DMO")
        self.horizontalLayout_6.addWidget(self.size_DMO)
        self.size_DMO.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.size_DMO.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.size_DMO).exec_(self.size_DMO.mapToGlobal(point)))

        self.allow_DMO = QtWidgets.QLineEdit(self.widget5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.allow_DMO.setFont(font)
        self.allow_DMO.setInputMethodHints(QtCore.Qt.ImhNone)
        self.allow_DMO.setMaxLength(32767)
        self.allow_DMO.setCursorPosition(0)
        self.allow_DMO.setAlignment(QtCore.Qt.AlignCenter)
        self.allow_DMO.setObjectName("allow_DMO")
        self.horizontalLayout_6.addWidget(self.allow_DMO)
        self.allow_DMO.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.allow_DMO.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.allow_DMO).exec_(self.allow_DMO.mapToGlobal(point)))

        self.pushButton = QtWidgets.QPushButton(self.main_frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 650, 401, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 1px solid white;\n"
"    background-color: rgba(255, 255, 255, 50)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.main_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 12, 433, 387))
        self.layoutWidget.setObjectName("layoutWidget")
        self.main_grid = QtWidgets.QGridLayout(self.layoutWidget)
        self.main_grid.setContentsMargins(0, 0, 0, 0)
        self.main_grid.setObjectName("main_grid")
        self.L_priority = QtWidgets.QLabel(self.layoutWidget)
        self.L_priority.setStyleSheet("border:none")
        self.L_priority.setObjectName("L_priority")
        self.main_grid.addWidget(self.L_priority, 0, 0, 1, 2)
        self.priority = QtWidgets.QComboBox(self.layoutWidget)
        self.priority.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.priority.setAutoFillBackground(False)
        self.priority.setStyleSheet("")
        self.priority.setMaxVisibleItems(103453556)
        self.priority.setFrame(True)
        self.priority.setObjectName("priority")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.main_grid.addWidget(self.priority, 0, 2, 1, 1)
        self.L_month = QtWidgets.QLabel(self.layoutWidget)
        self.L_month.setStyleSheet("border:none")
        self.L_month.setObjectName("L_month")
        self.main_grid.addWidget(self.L_month, 1, 0, 1, 1)
        self.month = QtWidgets.QComboBox(self.layoutWidget)
        self.month.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.month.setAutoFillBackground(False)
        self.month.setStyleSheet("")
        self.month.setMaxVisibleItems(103453556)
        self.month.setFrame(True)
        self.month.setObjectName("month")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.month.addItem("")
        self.main_grid.addWidget(self.month, 1, 2, 2, 1)
        self.L_filial = QtWidgets.QLabel(self.layoutWidget)
        self.L_filial.setStyleSheet("border:none")
        self.L_filial.setObjectName("L_filial")
        self.main_grid.addWidget(self.L_filial, 2, 0, 2, 1)
        self.filial = QtWidgets.QComboBox(self.layoutWidget)
        self.filial.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.filial.setAutoFillBackground(False)
        self.filial.setStyleSheet("")
        self.filial.setEditable(False)
        self.filial.setMaxVisibleItems(103453556)
        self.filial.setFrame(True)
        self.filial.setObjectName("filial")
        self.filial.addItem("")
        self.filial.addItem("")
        self.filial.addItem("")
        self.filial.addItem("")
        self.filial.addItem("")
        self.filial.addItem("")
        self.filial.addItem("")
        self.filial.addItem("")
        self.filial.addItem("")
        self.filial.addItem("")
        self.main_grid.addWidget(self.filial, 3, 2, 1, 1)
        self.L_district = QtWidgets.QLabel(self.layoutWidget)
        self.L_district.setStyleSheet("border:none")
        self.L_district.setObjectName("L_district")
        self.main_grid.addWidget(self.L_district, 4, 0, 1, 1)

        self.district = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.district.setFont(font)
        self.district.setInputMethodHints(QtCore.Qt.ImhNone)
        self.district.setMaxLength(3)
        self.district.setAlignment(QtCore.Qt.AlignCenter)
        self.district.setObjectName("district")
        self.main_grid.addWidget(self.district, 4, 2, 1, 1)
        self.district.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.district.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.district).exec_(self.district.mapToGlobal(point)))

        self.L_snils = QtWidgets.QLabel(self.layoutWidget)
        self.L_snils.setStyleSheet("border:none")
        self.L_snils.setObjectName("L_snils")
        self.main_grid.addWidget(self.L_snils, 5, 0, 1, 1)
        self.L_FIO = QtWidgets.QLabel(self.layoutWidget)
        self.L_FIO.setStyleSheet("border:none")
        self.L_FIO.setObjectName("L_FIO")
        self.main_grid.addWidget(self.L_FIO, 6, 0, 1, 1)
        self.L_operation = QtWidgets.QLabel(self.layoutWidget)
        self.L_operation.setStyleSheet("border:none")
        self.L_operation.setObjectName("L_operation")
        self.main_grid.addWidget(self.L_operation, 7, 0, 1, 1)
        self.operation_type = QtWidgets.QComboBox(self.layoutWidget)
        self.operation_type.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.operation_type.setAutoFillBackground(False)
        self.operation_type.setStyleSheet("")
        self.operation_type.setEditable(False)
        self.operation_type.setMaxVisibleItems(103453556)
        self.operation_type.setFrame(True)
        self.operation_type.setObjectName("operation_type")
        self.operation_type.addItem("")
        self.operation_type.addItem("")
        self.operation_type.addItem("")
        self.main_grid.addWidget(self.operation_type, 7, 2, 1, 1)
        self.L_bank = QtWidgets.QLabel(self.layoutWidget)
        self.L_bank.setStyleSheet("border:none")
        self.L_bank.setObjectName("L_bank")
        self.main_grid.addWidget(self.L_bank, 8, 0, 1, 1)


        self.add_bank = QtWidgets.QToolButton(self.layoutWidget)
        self.add_bank.setObjectName("add_bank")
        self.add_bank.clicked.connect(self.open_bank_dialog)

        self.main_grid.addWidget(self.add_bank, 8, 3, 1, 1)
        self.L_specialist = QtWidgets.QLabel(self.layoutWidget)
        self.L_specialist.setStyleSheet("border:none")
        self.L_specialist.setObjectName("L_specialist")
        self.main_grid.addWidget(self.L_specialist, 9, 0, 1, 1)
        self.L_note = QtWidgets.QLabel(self.layoutWidget)
        self.L_note.setStyleSheet("border:none")
        self.L_note.setObjectName("L_note")
        self.main_grid.addWidget(self.L_note, 10, 0, 1, 1)
        self.L_wdate = QtWidgets.QLabel(self.layoutWidget)
        self.L_wdate.setStyleSheet("border:none")
        self.L_wdate.setObjectName("L_wdate")
        self.main_grid.addWidget(self.L_wdate, 11, 0, 1, 1)
        self.wdate = QtWidgets.QDateEdit(self.layoutWidget)
        self.wdate.setStyleSheet("QDateEdit {\n"
"    background-color: white;\n"
"}\n"
"\n"
"")
        self.wdate.setAlignment(QtCore.Qt.AlignCenter)
        self.wdate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 14), QtCore.QTime(0, 0, 0)))
        self.wdate.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.wdate.setCalendarPopup(True)
        self.wdate.setDate(datetime.today())
        self.wdate.setObjectName("wdate")
        self.main_grid.addWidget(self.wdate, 11, 2, 1, 1)

        self.snils = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.snils.setFont(font)
        self.snils.setInputMethodHints(QtCore.Qt.ImhNone)
        self.snils.setMaxLength(14)
        self.snils.setCursorPosition(14)
        self.snils.setAlignment(QtCore.Qt.AlignCenter)
        self.snils.setPlaceholderText("")
        self.snils.setObjectName("snils")
        self.main_grid.addWidget(self.snils, 5, 2, 1, 1)
        self.snils.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.snils.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.snils).exec_(self.snils.mapToGlobal(point)))

        self.fio_pens = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.fio_pens.setFont(font)
        self.fio_pens.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fio_pens.setMaxLength(32767)
        self.fio_pens.setCursorPosition(0)
        self.fio_pens.setAlignment(QtCore.Qt.AlignCenter)
        self.fio_pens.setObjectName("fio_pens")
        self.main_grid.addWidget(self.fio_pens, 6, 2, 1, 1)
        self.fio_pens.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.fio_pens.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.fio_pens).exec_(self.fio_pens.mapToGlobal(point)))

        self.bank = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.bank.setFont(font)
        self.bank.setInputMethodHints(QtCore.Qt.ImhNone)
        self.bank.setMaxLength(32767)
        self.bank.setCursorPosition(0)
        self.bank.setAlignment(QtCore.Qt.AlignCenter)
        self.bank.setObjectName("bank")
        self.bank.setReadOnly(True)
        self.main_grid.addWidget(self.bank, 8, 2, 1, 1)
        self.specialist = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.specialist.setFont(font)
        self.specialist.setInputMethodHints(QtCore.Qt.ImhNone)
        self.specialist.setMaxLength(32767)
        self.specialist.setCursorPosition(0)
        self.specialist.setAlignment(QtCore.Qt.AlignCenter)
        self.specialist.setObjectName("specialist")
        self.main_grid.addWidget(self.specialist, 9, 2, 1, 1)
        self.specialist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.specialist.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.specialist).exec_(self.specialist.mapToGlobal(point)))

        self.note = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.note.setFont(font)
        self.note.setInputMethodHints(QtCore.Qt.ImhNone)
        self.note.setMaxLength(32767)
        self.note.setCursorPosition(0)
        self.note.setAlignment(QtCore.Qt.AlignCenter)
        self.note.setObjectName("note")
        self.main_grid.addWidget(self.note, 10, 2, 1, 1)
        self.note.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.note.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.note).exec_(self.note.mapToGlobal(point)))

        self.retranslateUi(NewRecord)
        QtCore.QMetaObject.connectSlotsByName(NewRecord)

    def open_bank_dialog(self):
        self.bank_dialog = Ui_Dialog(self.logger, self.user)
        self.bank_window = QtWidgets.QDialog()
        self.bank_dialog.setupUi(self.bank_window)
        self.bank_window.show()
        self.bank_dialog.banks_list.doubleClicked.connect(self.on_bank_selected)

    def on_bank_selected(self, index):
        selected_bank = index.data()
        self.bank.setText(selected_bank)
        self.bank_window.close()

    def retranslateUi(self, NewRecord):
        table_delegate = TableItemDelegate(self.main_frame)
        self.priority.setItemDelegate(table_delegate)
        self.month.setItemDelegate(table_delegate)
        self.filial.setItemDelegate(table_delegate)
        self.operation_type.setItemDelegate(table_delegate)

        _translate = QtCore.QCoreApplication.translate
        NewRecord.setWindowTitle(_translate("NewRecord", "Новая запись"))
        self.label_new_record.setText(_translate("NewRecord", "Новая запись"))
        self.L_sizePens.setText(_translate("NewRecord", "Уст. Размер Пенсии:"))
        self.L_allowPens.setText(_translate("NewRecord", "Доплата Пенсии:"))
        self.L_sizeEDV.setText(_translate("NewRecord", "Уст. Размер ЕДВ:"))
        self.L_allowEDV.setText(_translate("NewRecord", "Доплата ЕДВ:"))
        self.L_sizeDMO.setText(_translate("NewRecord", "Уст. Размер ДМО:"))
        self.L_allowDMO.setText(_translate("NewRecord", "Доплата ДМО:"))
        self.pushButton.setText(_translate("NewRecord", "Сохранить"))
        self.L_priority.setText(_translate("NewRecord", "*Очередность выплаты:"))
        self.priority.setCurrentText(_translate("NewRecord", "Основная"))
        self.priority.setItemText(0, _translate("NewRecord", "Основная"))
        self.priority.setItemText(1, _translate("NewRecord", "Доп. 1"))
        self.priority.setItemText(2, _translate("NewRecord", "Разовая 1"))
        self.priority.setItemText(3, _translate("NewRecord", "Разовая 2"))
        self.priority.setItemText(4, _translate("NewRecord", "Разовая 3"))
        self.priority.setItemText(5, _translate("NewRecord", "Разовая 4"))
        self.priority.setItemText(6, _translate("NewRecord", "Разовая 5"))
        self.priority.setItemText(7, _translate("NewRecord", "Разовая 6"))
        self.L_month.setText(_translate("NewRecord", "*Выплатной месяц:"))
        self.month.setCurrentText(_translate("NewRecord", "Январь"))
        self.month.setItemText(0, _translate("NewRecord", "Январь"))
        self.month.setItemText(1, _translate("NewRecord", "Февраль"))
        self.month.setItemText(2, _translate("NewRecord", "Март"))
        self.month.setItemText(3, _translate("NewRecord", "Апрель"))
        self.month.setItemText(4, _translate("NewRecord", "Май"))
        self.month.setItemText(5, _translate("NewRecord", "Июнь"))
        self.month.setItemText(6, _translate("NewRecord", "Июль"))
        self.month.setItemText(7, _translate("NewRecord", "Август"))
        self.month.setItemText(8, _translate("NewRecord", "Сентябрь"))
        self.month.setItemText(9, _translate("NewRecord", "Октябрь"))
        self.month.setItemText(10, _translate("NewRecord", "Ноябрь"))
        self.month.setItemText(11, _translate("NewRecord", "Декабрь"))
        self.L_filial.setText(_translate("NewRecord", "*№ Филиала:"))
        self.filial.setCurrentText(_translate("NewRecord", "Ф-л 1"))
        self.filial.setItemText(0, _translate("NewRecord", "Ф-л 1"))
        self.filial.setItemText(1, _translate("NewRecord", "Ф-л 2"))
        self.filial.setItemText(2, _translate("NewRecord", "Ф-л 3"))
        self.filial.setItemText(3, _translate("NewRecord", "Ф-л 4"))
        self.filial.setItemText(4, _translate("NewRecord", "Ф-л 5"))
        self.filial.setItemText(5, _translate("NewRecord", "Ф-л 6"))
        self.filial.setItemText(6, _translate("NewRecord", "Ф-л 7"))
        self.filial.setItemText(7, _translate("NewRecord", "Ф-л 8"))
        self.filial.setItemText(8, _translate("NewRecord", "Ф-л 9"))
        self.filial.setItemText(9, _translate("NewRecord", "Ф-л 10"))
        self.L_district.setText(_translate("NewRecord", "*Район:"))
        self.L_snils.setText(_translate("NewRecord", "*СНИЛС:"))
        self.L_FIO.setText(_translate("NewRecord", "*ФИО ПЕНСИОНЕРА:"))
        self.L_operation.setText(_translate("NewRecord", "*Операция:"))
        self.operation_type.setCurrentText(_translate("NewRecord", "Назначение"))
        self.operation_type.setItemText(0, _translate("NewRecord", "Назначение"))
        self.operation_type.setItemText(1, _translate("NewRecord", "Постановка"))
        self.operation_type.setItemText(2, _translate("NewRecord", "Перерасчет"))
        self.L_bank.setText(_translate("NewRecord", "*Дост. организация:"))
        self.add_bank.setText(_translate("NewRecord", "+"))
        self.L_specialist.setText(_translate("NewRecord", "*Специалист О.В.:"))
        self.L_note.setText(_translate("NewRecord", "Примечание:"))
        self.L_wdate.setText(_translate("NewRecord", "*Дата отработки:"))
        self.snils.setInputMask(_translate("NewRecord", "XXX-XXX-XXX XX"))
        self.snils.setText(_translate("NewRecord", "___-___-___ __"))
        self.fio_pens.setPlaceholderText(_translate("NewRecord", "Фамилия И.О."))

        self.priority.setCurrentIndex(-1)
        self.month.setCurrentIndex(-1)
        self.filial.setCurrentIndex(-1)
        self.operation_type.setCurrentIndex(-1)

        # Ручная настройка

        # Запрет на ввод букв
        onlyInt = QtGui.QIntValidator()
        self.district.setValidator(onlyInt)

        # Запрет на ввод букв и иных значений для СНИЛС
        regexSNILS = QRegExp("[0-9\-_ ]+")
        validator = QRegExpValidator(regexSNILS)
        self.snils.setValidator(validator)

        # Запрет на ввод букв и иных значений для сумм
        regexSumm = QRegExp("[0-9]+[,|.][0-9]{2}")
        validator = QRegExpValidator(regexSumm)
        self.size_Pens.setValidator(validator)
        self.size_EDV.setValidator(validator)
        self.size_DMO.setValidator(validator)
        self.allow_Pens.setValidator(validator)
        self.allow_EDV.setValidator(validator)
        self.allow_DMO.setValidator(validator)

    def showContextMenu(self, line_edit):
        menu = QMenu(line_edit)
        menu.addAction("Копировать").triggered.connect(line_edit.copy)
        menu.addAction("Вырезать").triggered.connect(line_edit.cut)
        menu.addAction("Вставить").triggered.connect(line_edit.paste)
        return menu

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewRecord = QtWidgets.QDialog()
    ui = Ui_NewRecord()
    ui.setupUi(NewRecord)
    NewRecord.show()
    sys.exit(app.exec_())