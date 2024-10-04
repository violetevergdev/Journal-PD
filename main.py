import os
import sys
from datetime import datetime
import ctypes

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from modules.gui.window.ui_main import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog, QMessageBox

from configuration.config import settings as conf

from modules.gui.window.new_record import Ui_NewRecord
from modules.gui.window.find_wind import Ui_Find_MainWindow
from modules.db.db_connection import Database
from modules.optionally.clear_fields import clear_fields
from modules.optionally.delegates import TableItemDelegate
from modules.optionally.get_entry_data import get_entry_data
from modules.optionally.validate_data import validate_data
from modules.optionally.unload_XLSX_data import unload_XLSX_data

from modules.optionally.logging_db import logging_db

class Journal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Journal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.unloadXLSXAction.triggered.connect(self.unload_XLSX_records)
        self.ui.updateTableAction.triggered.connect(self.view_data)
        self.ui.findAction.triggered.connect(self.open_find_window)

        self.db = Database(self)
        self._CP = conf.CP
        self._UNLOADP = conf.UNP
        self.logger = logging_db()
        self.user = os.getlogin()
        self.view_data()
        self.ui.add_btn.clicked.connect(self.open_new_record_window)
        self.ui.delete_btn.clicked.connect(self.delete_record)
        self.ui.edit_btn.clicked.connect(self.edit_record)

    def view_data(self):
        self.model = QStandardItemModel(self)

        query, cursor = self.db.get_data_for_view(self.logger, self.user)

        if query or query == []:
            self.model.setHorizontalHeaderLabels([col[0] for col in cursor.description])
            for row_data in query:
                items = [QStandardItem(str(field)) for field in row_data]
                self.model.appendRow(items)
            self.ui.table.setModel(self.model)

            # Центрируем текст ячеек по центру и приводим числовые значения в порядок
            table_delegate = TableItemDelegate(self.ui.table)
            self.ui.table.setItemDelegate(table_delegate)

            # Уст ширину колонок по содержимому
            self.ui.table.resizeColumnsToContents()

            # Убираем вертикальный heder
            self.ui.table.verticalHeader().hide()

            # Убираем highlight с горизонтаьного заголовка при выборе записи
            self.ui.table.horizontalHeader().setHighlightSections(False)

            # Устанавливаем выбор всей строки
            self.ui.table.setSelectionBehavior(QAbstractItemView.SelectRows)

            # Отключаем редактирвоание данных двойным нажатием
            self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        else:
            QMessageBox.critical(self, 'Ошибка', 'Ошибка при прочтении базы данных')

    def open_new_record_window(self):
        self.new_window = QtWidgets.QDialog(self)
        self.ui_window = Ui_NewRecord(self.logger, self.user)
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()

        if sender.text() in ('Добавить', 'Изменить'):
            self.ui_window.pushButton.clicked.connect(lambda: self.add_record(sender.text()))

    def add_record(self, type_operation):
        data = get_entry_data(self)

        if validate_data(self, data):
            if type_operation == 'Добавить':
                if self.db.add_new_record(self.logger, self.user, data):
                    self.logger.info(
                        f'\n[ADD] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - Запись успешно добавлена '
                        f'пользователем {self.user}, данные записи: {data}')
                    clear_fields(self)

            if type_operation == 'Изменить':
                if self.db.update_record(self.logger, self.user, data, self.edit_id):
                    self.logger.info(
                        f'\n[EDIT] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - Запись успешно изменена '
                        f'пользователем {self.user}, данные записи: {data}')
                    self.new_window.close()
                    QMessageBox.information(self, 'Успех', 'Запись была успешно изменена')
            self.view_data()
        else:
            self.new_window.activateWindow()

    def delete_record(self):
        row = self.ui.table.selectedIndexes()
        if row:
            password, ok = QInputDialog.getText(self, 'Подтверждение удаления', 'Введите пароль:')
            if ok:
                if password == self._CP:
                    id = str(self.ui.table.model().data(row[0]))
                    snils = str(self.ui.table.model().data(row[5]))
                    fio_pens = str(self.ui.table.model().data(row[6]))
                    specialist = str(self.ui.table.model().data(row[15]))

                    if self.db.delete_record(self.logger, self.user, id):
                        self.logger.info(
                            f'\n[DELETE] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - Запись успешно удалена '
                            f'пользователем {self.user}, данные записи: СНИЛС - {snils}, '
                            f'ФИО Пенсионера - {fio_pens}, Специалист - {specialist}')
                        self.view_data()
                        QMessageBox.information(self, 'Успех', 'Запись была успешно удалена')
                else:
                    QMessageBox.critical(self, 'Ошибка', 'Неправильный пароль')
        else:
            QMessageBox.warning(self, "Внимание", "Выберите запись")

    def edit_record(self):
        row_vales = self.ui.table.selectedIndexes()
        if row_vales:
            self.open_new_record_window()
            for id, val in enumerate(row_vales):
                insert_data = str(self.ui.table.model().data(val))
                if id == 0:
                    self.edit_id = insert_data
                elif id == 1:
                    self.ui_window.priority.setCurrentText(insert_data)
                elif id == 2:
                    self.ui_window.month.setCurrentText(insert_data)
                elif id == 3:
                    self.ui_window.filial.setCurrentText(insert_data)
                elif id == 4:
                    self.ui_window.district.setText(insert_data)
                elif id == 5:
                    self.ui_window.snils.setText(insert_data)
                elif id == 6:
                    self.ui_window.fio_pens.setText(insert_data)
                elif id == 7:
                    self.ui_window.operation_type.setCurrentText(insert_data)
                elif id == 8:
                    self.ui_window.size_Pens.setText(insert_data)
                elif id == 9:
                    self.ui_window.allow_Pens.setText(insert_data)
                elif id == 10:
                    self.ui_window.size_EDV.setText(insert_data)
                elif id == 11:
                    self.ui_window.allow_EDV.setText(insert_data)
                elif id == 12:
                    self.ui_window.size_DMO.setText(insert_data)
                elif id == 13:
                    self.ui_window.allow_DMO.setText(insert_data)
                elif id == 14:
                    self.ui_window.bank.setText(insert_data)
                elif id == 15:
                    self.ui_window.specialist.setText(insert_data)
                elif id == 16:
                    self.ui_window.note.setText(insert_data)
                elif id == 17:
                    date_format = "%d.%m.%Y"
                    insert_datetime = datetime.strptime(insert_data, date_format)
                    self.ui_window.wdate.setDate(datetime.date(insert_datetime))

        else:
            QMessageBox.warning(self, "Внимание", "Выберите запись")

    def unload_XLSX_records(self):
        password, ok = QInputDialog.getText(self, 'Подтверждение прав', 'Введите пароль:')
        if ok:
            if password == self._UNLOADP:
                try:
                    data, cursor = self.db.get_all_records(self.logger, self.user)
                    if data:
                        unload_XLSX_data(data, cursor)
                        self.logger.info(
                            f'\n[UNLOAD] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - Таблица успешно '
                            f'выгружена пользователем {self.user}')
                        QMessageBox.information(None, "Выгрузка в XLSX", "Данные успешно выгружены")
                except Exception as e:
                    print(e)
            else:
                QMessageBox.critical(self, 'Ошибка', 'Неправильный пароль')

    def open_find_window(self):
        self.find_window = QtWidgets.QDialog(self)
        self.ui_find_window = Ui_Find_MainWindow()
        self.ui_find_window.setupUi(self.find_window)
        self.find_window.show()

        self.ui_find_window.pushButton.clicked.connect(self.find_records)

    def find_records(self):
        selected_column = self.ui_find_window.comboBox.currentText()
        value = self.ui_find_window.lineEdit.text()

        if selected_column:
            query, cursor = self.db.find_records(self.logger, self.user, selected_column, value)

            self.model = QStandardItemModel(self)

            if query:
                self.model.setHorizontalHeaderLabels([col[0] for col in cursor.description])
                for row_data in query:
                    items = [QStandardItem(str(field)) for field in row_data]
                    self.model.appendRow(items)
                self.ui.table.setModel(self.model)
            else:
                QMessageBox.information(self, 'Записей нет', 'Запись не была найдена')



if __name__ == '__main__':
    if conf.ENV_FOR_DYNACONF == 'prod':
        import pyi_splash
        pyi_splash.close()

    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)

    if conf.ENV_FOR_DYNACONF == 'prod':
        db_path = os.path.join(sys._MEIPASS, 'icon.ico')
        app.setWindowIcon(QIcon(db_path))

    main = Journal()

    main.show()
    sys.exit(app.exec_())
