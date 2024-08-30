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

    def run_query(self, sql_query, params=None):
        query = QSqlQuery()
        query.prepare(sql_query)

        if params is not None:
            for param in params:
                query.addBindValue(param)

        if not query.exec():
            QMessageBox.critical(self.parent, "Ошибка ", "Ошибка при выполнении запроса", QMessageBox.Ok)

        return query

    def get_all_records(self):
        sql_query = 'SELECT * FROM pfr'
        result = self.run_query(sql_query)
        return result

    def add_new_record(self, record_values):
        sql_query = "INSERT INTO pfr VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.run_query(sql_query, record_values)

    def update_record(self, record_values, id_el):
        sql_query = f'''UPDATE pfr SET 'Очередность выплаты' = ?, 'Выплатной месяц' = ?, '№ Филиала' = ?,
                     Район = ?, СНИЛС = ?, 'ФИО Пенсионера' = ?, Операция = ?, 'УСТ Размер пенсии' = ?, 
                     'Доплата ПЕНС' = ?, 'УСТ Размер ЕДВ' = ?, 'Доплата ЕДВ' = ?, 'УСТ Размер ДМО' = ?, 
                    'Доплата ДМО' = ?, 'Доставочная организация' = ?, 'Специалист ОВ' = ?, Примечание = ?, 'Дата отработки' = ? 
                    WHERE id = {id_el}'''

        self.run_query(sql_query, record_values)

    def delete_record(self, id_el):
        sql_query = 'DELETE FROM pfr WHERE id = ?'
        self.run_query(sql_query, (id_el,))

    def get_banks(self):
        query_bank = 'SELECT * FROM banks'
        result_bank = self.run_query(query_bank)

        data_list = []
        while result_bank.next():
            data_string = str(result_bank.value(0))
            data_list.append(data_string)

        return data_list

    def add_bank(self, val):
        sql_query = 'INSERT INTO banks VALUES (?)'
        self.run_query(sql_query, (val,))

    def find_records(self, selected_column, value):
        sql_query = f"SELECT * FROM pfr WHERE \"{selected_column}\" LIKE '%{value}%'"
        query = self.run_query(sql_query)
        return query

