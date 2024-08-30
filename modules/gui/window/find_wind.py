# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/find-wind.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu


class Ui_Find_MainWindow(object):
    def setupUi(self, Find_MainWindow):
        Find_MainWindow.setObjectName("Find_MainWindow")
        Find_MainWindow.resize(548, 176)
        Find_MainWindow.setStyleSheet("QDialog {\n"
"  background-color: #93a5a7;\n"
"}")
        self.frame = QtWidgets.QFrame(Find_MainWindow)
        self.frame.setGeometry(QtCore.QRect(30, 50, 491, 101))
        self.frame.setStyleSheet("QFrame {\n"
"    border: 1px solid white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(21, 21, 201, 30))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    font-size: 20px;\n"
"    font-family: \'Calibri\';\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(240, 21, 231, 29))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    font-size: 18px;\n"
"    font-family:\'Calibri\';\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 60, 111, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #93a5a7;\n"
"    border: 1px solid white;\n"
"    font-size: 18px;\n"
"    font-family: \'Calibri\';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#a8b7b8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #bec9ca;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Find_MainWindow)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 31))
        self.label.setStyleSheet("QLabel {\n"
"    font-size: 20px;\n"
"    font-family: \'Calibri\';\n"
"    color: white;\n"
"}")
        self.label.setObjectName("label")

        self.lineEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lineEdit.customContextMenuRequested.connect(
            lambda point: self.showContextMenu(self.lineEdit).exec_(self.lineEdit.mapToGlobal(point)))

        self.retranslateUi(Find_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Find_MainWindow)

    def retranslateUi(self, Find_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Find_MainWindow.setWindowTitle(_translate("Find_MainWindow", "Поиск"))
        self.lineEdit.setPlaceholderText(_translate("Find_MainWindow", "Ввод"))
        self.comboBox.setItemText(0, _translate("Find_MainWindow", "СНИЛС"))
        self.comboBox.setItemText(1, _translate("Find_MainWindow", "ФИО Пенсионера"))
        self.comboBox.setItemText(2, _translate("Find_MainWindow", "Специалист ОВ"))
        self.comboBox.setItemText(3, _translate("Find_MainWindow", "№ Филиала"))
        self.comboBox.setItemText(4, _translate("Find_MainWindow", "Район"))
        self.comboBox.setItemText(5, _translate("Find_MainWindow", "Доставочная организация"))
        self.comboBox.setItemText(6, _translate("Find_MainWindow", "Очередность выплаты"))
        self.comboBox.setItemText(7, _translate("Find_MainWindow", "Выплатной месяц"))
        self.pushButton.setText(_translate("Find_MainWindow", "Найти"))
        self.label.setText(_translate("Find_MainWindow", "Поиск"))

    def showContextMenu(self, line_edit):
        menu = QMenu(line_edit)
        menu.addAction("Копировать").triggered.connect(line_edit.copy)
        menu.addAction("Вырезать").triggered.connect(line_edit.cut)
        menu.addAction("Вставить").triggered.connect(line_edit.paste)
        return menu









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Find_MainWindow = QtWidgets.QDialog()
    ui = Ui_Find_MainWindow()
    ui.setupUi(Find_MainWindow)
    Find_MainWindow.show()
    sys.exit(app.exec_())