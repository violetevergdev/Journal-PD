from datetime import datetime

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox


class Database:
    def __init__(self, parent):
        self.db = None
        self.parent = parent

    def connect(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("W:\\!VIOLETTA!\\!fw!\\journal\\journal.db")
        # self.db.setDatabaseName("pfr.db")
        if not self.db.open():
            QMessageBox.critical(self.parent, "Ошибка ", "Невозможно подключиться к базе данных", QMessageBox.Ok)

    def disconnect(self):
        self.db.close()

    def run_query(self, sql_query, logger, user, params=None):
        query = QSqlQuery()
        query.prepare(sql_query)

        if params is not None:
            for param in params:
                query.addBindValue(param)

        if not self.db.transaction():
            QMessageBox.critical(self.parent, "Ошибка", "Не удалось начать транзакцию", QMessageBox.Ok)
            logger.error(
                f'\n[ERR-TRANSACTION] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - Не удалось начать транзакцию, '
                f'пользователь {user}, данные записи: {params}\nОШИБКА:{query.lastError().text()}')
            return None

        if not query.exec():
            QMessageBox.critical(self.parent, "Ошибка ", "Ошибка при выполнении запроса", QMessageBox.Ok)
            logger.error(
                f'\n[ERR-QUERY] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - Ошибка при выполнении запроса, '
                f'пользователь {user}, данные записи: {params}\nОШИБКА:{query.lastError().text()}')
            return None

        if not self.db.commit():
            QMessageBox.critical(self.parent, "Ошибка", "Не удалось завершить транзакцию", QMessageBox.Ok)
            logger.error(
                f'\n[ERR-TRANSACTION] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - Не удалось завершить транзакцию, '
                f'пользователь {user}, данные записи: {params}\nОШИБКА:{query.lastError().text()}')
            return None

        return query

    def add_new_record(self, logger, user, record_values):
        self.connect()
        sql_query = "INSERT INTO pfr VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        result = self.run_query(sql_query, logger, user, record_values)
        self.disconnect()
        if result is None:
            return False
        else:
            return True

    def update_record(self, logger, user, record_values, id_el):
        self.connect()
        sql_query = f'''UPDATE pfr SET 'Очередность выплаты' = ?, 'Выплатной месяц' = ?, '№ Филиала' = ?,
                     Район = ?, СНИЛС = ?, 'ФИО Пенсионера' = ?, Операция = ?, 'УСТ Размер пенсии' = ?, 
                     'Доплата ПЕНС' = ?, 'УСТ Размер ЕДВ' = ?, 'Доплата ЕДВ' = ?, 'УСТ Размер ДМО' = ?, 
                    'Доплата ДМО' = ?, 'Доставочная организация' = ?, 'Специалист ОВ' = ?, Примечание = ?, 'Дата отработки' = ? 
                    WHERE id = {id_el}'''

        result = self.run_query(sql_query, logger, user, record_values)
        self.disconnect()
        if result is None:
            return False
        else:
            return True

    def delete_record(self, logger, user, id_el):
        self.connect()
        sql_query = 'DELETE FROM pfr WHERE id = ?'
        result = self.run_query(sql_query, logger, user, (id_el,))
        self.disconnect()
        if result is None:
            return False
        else:
            return True

    def get_banks(self, logger, user):
        self.connect()
        query_bank = 'SELECT * FROM banks'
        result_bank = self.run_query(query_bank, logger, user)

        data_list = []
        while result_bank.next():
            data_string = str(result_bank.value(0))
            data_list.append(data_string)

        self.disconnect()
        return data_list

    def add_bank(self, logger, user, val):
        self.connect()

        sql_query = 'INSERT INTO banks VALUES (?)'
        result = self.run_query(sql_query, logger, user, (val,))
        self.disconnect()
        if result is None:
            return False
        else:
            return True

    def find_records(self, logger, user, selected_column, value):
        sql_query = f"SELECT * FROM pfr WHERE \"{selected_column}\" LIKE '%{value}%'"
        query = self.run_query(sql_query, logger, user)

        return query

