# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QAction


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {background-color: white}\n"
                                         "QPushButton {\n"
                                         "    background-color: #93a5a7;\n"
                                         "    border: 1px solid #dbdad5\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgba(147,165,167, 0.8);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgba(147,165,167, 0.3);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")

        # Создаем Layout в котором будем позиционировать элементы
        layout = QtWidgets.QVBoxLayout(self.centralwidget)

        horizontal_layout = QtWidgets.QHBoxLayout()

        self.main_label_journal = QtWidgets.QLabel(self.centralwidget)
        self.main_label_journal.setGeometry(QtCore.QRect(10, 0, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.main_label_journal.setFont(font)
        self.main_label_journal.setObjectName("main_label_journal")

        self.main_label_vers = QtWidgets.QLabel(self.centralwidget)
        self.main_label_vers.setGeometry(QtCore.QRect(1050, 0, 60, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.main_label_vers.setStyleSheet("color: gray;")
        self.main_label_vers.setFont(font)
        self.main_label_vers.setObjectName("main_label_vers")

        horizontal_layout.addWidget(self.main_label_journal)
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.main_label_vers, alignment=QtCore.Qt.AlignRight)

        layout.addLayout(horizontal_layout)

        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 50, 1091, 601))
        self.table.setObjectName("table")
        self.table.setStyleSheet(u"QTableView {\n"
                                 "border: 3px solid #93a5a7;\n"
                                 "border-radius: 3px; \n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section {\n"
                                 "background-color: #93a5a7;\n"
                                 "font-size: 15px;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView::item {\n"
                                 "text-align: center; \n"
                                 "border: 1px solid gray; \n"
                                 "border-top: none; \n"
                                 "border-right: none; \n"
                                 "}\n"
                                 "\n"
                                 "QTableView::item:selected{\n"
                                 "background-color: #849496;\n"
                                 "}\n"
                                 "")
        # Установка шрифта для ячеек
        fnt = self.table.font()
        fnt.setPointSize(12)
        self.table.setFont(fnt)

        # Добавляем таблицу в layout
        layout.addWidget(self.table)

        # ===========================Кнопки===================================================
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 660, 1081, 81))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Добавляем horizontalLayout с кнопками в layout
        layout.addWidget(self.widget)

        self.add_btn = QtWidgets.QPushButton(self.widget)
        self.add_btn.setMinimumHeight(90)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.delete_btn = QtWidgets.QPushButton(self.widget)
        self.delete_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.edit_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_btn.sizePolicy().hasHeightForWidth())
        self.edit_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.edit_btn.setFont(font)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout.addWidget(self.edit_btn)
        # =====================================================================================================
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = MainWindow.menuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")

        self.unloadXLSXAction = QAction('&Выгрузить', MainWindow)
        self.unloadXLSXAction.setStatusTip('Выгрузить')

        self.updateTableAction = QAction('&Обновить', MainWindow)
        self.updateTableAction.setStatusTip('Обновить')

        self.findAction = QAction('&Поиск', MainWindow)
        self.findAction.setStatusTip('Поиск')

        self.menubar.addAction(self.unloadXLSXAction)
        self.menubar.addAction(self.updateTableAction)
        self.menubar.addAction(self.findAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Журнал ПД"))
        self.main_label_journal.setText(_translate("MainWindow", "Журнал пенсионных дел"))
        self.main_label_vers.setText(_translate("MainWindow", MainWindow.vers))
        self.add_btn.setText(_translate("MainWindow", "Добавить"))
        self.delete_btn.setText(_translate("MainWindow", "Удалить"))
        self.edit_btn.setText(_translate("MainWindow", "Изменить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
