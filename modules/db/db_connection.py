import sqlite3
import threading
import time
from datetime import datetime

from PyQt5.QtWidgets import QMessageBox

from configuration.config import settings as conf
from modules.optionally.logging_db import logging_db


class Database:
    def __init__(self, parent):
        self.parent = parent

    def run_query(self, sql_query, logger, user, parameters=(), retries=3, wait_time=0.5):
        attempt = 0
        while attempt < retries:
            try:
                conf.reload()
                with sqlite3.connect(conf.db_path) as conn:
                    conn.execute('PRAGMA journal_mode=WAL')
                    curs = conn.cursor()
                    result = curs.execute(sql_query, parameters)
                    conn.commit()
                    return result, curs
            except sqlite3.OperationalError as e:
                if 'database is locked' in str(e):
                    attempt += 1
                    time.sleep(wait_time)
                    if attempt == retries:
                        QMessageBox.critical(self.parent, "Ошибка", "База данных заблокирована. Попробуйте позже.",
                                             QMessageBox.Ok)
                        logger.error(
                            f'\n[ERR-QUERY] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - База данных заблокирована, '
                            f'пользователь {user}, данные записи: {parameters}\nОШИБКА: {e}')
                        return None
                else:
                    QMessageBox.critical(self.parent, "Ошибка ", "Ошибка при выполнении запроса: " + str(e),
                                         QMessageBox.Ok)
                    logger.error(
                        f'\n[ERR-QUERY] {str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))} - Ошибка при выполнении запроса, '
                        f'пользователь {user}, данные записи: {parameters}\nОШИБКА: {e}')
                    return None

    def get_data_for_view(self, logger, user):
        try:
            sql_query = 'SELECT * FROM pfr ORDER BY id DESC LIMIT 2000'
            result, cursor = self.run_query(sql_query, logger, user)
            if result is None:
                return False
            else:
                data_list = [name for name in result]
                return data_list, cursor
        except Exception:
            return False


    def get_all_records(self, logger, user):
        try:
            sql_query = 'SELECT * FROM pfr'
            result, cursor = self.run_query(sql_query, logger, user)
            if result is None:
                return False
            else:
                data_list = [name for name in result]
                return data_list, cursor
        except Exception:
            return False


    def add_new_record(self, logger, user, record_values):
        try:
            sql_query = "INSERT INTO pfr VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            result, _ = self.run_query(sql_query, logger, user, record_values)
            if result is None:
                return False
            else:
                return True
        except Exception:
            return False


    def update_record(self, logger, user, record_values, id_el):
        try:
            sql_query = f'''UPDATE pfr SET 'Очередность выплаты' = ?, 'Выплатной месяц' = ?, '№ Филиала' = ?,
                         Район = ?, СНИЛС = ?, 'ФИО Пенсионера' = ?, Операция = ?, 'УСТ Размер пенсии' = ?,
                         'Доплата ПЕНС' = ?, 'УСТ Размер ЕДВ' = ?, 'Доплата ЕДВ' = ?, 'УСТ Размер ДМО' = ?,
                        'Доплата ДМО' = ?, 'Доставочная организация' = ?, 'Специалист ОВ' = ?, Примечание = ?, 'Дата отработки' = ?
                        WHERE id = {id_el}'''

            result, _ = self.run_query(sql_query, logger, user, record_values)
            if result is None:
                return False
            else:
                return True
        except Exception:
            return False


    def delete_record(self, logger, user, id_el):
        try:
            sql_query = 'DELETE FROM pfr WHERE id = ?'
            result, _ = self.run_query(sql_query, logger, user, (id_el,))
            if result is None:
                return False
            else:
                return True
        except Exception:
            return False


    def get_banks(self, logger, user):
        try:
            query_bank = 'SELECT * FROM banks'
            result_bank, _ = self.run_query(query_bank, logger, user)

            data_list = [name[0].upper() for name in result_bank]

            return data_list
        except Exception:
            return False


    def add_bank(self, logger, user, val):
        try:
            sql_query = 'INSERT INTO banks VALUES (?)'
            result, _ = self.run_query(sql_query, logger, user, (val,))
            if result is None:
                return False
            else:
                return True
        except Exception:
            return False


    def find_records(self, logger, user, selected_column, value):
        try:
            sql_query = f"SELECT * FROM pfr WHERE \"{selected_column}\" LIKE '%{value}%'"
            query, cursor = self.run_query(sql_query, logger, user)

            if query is None:
                return False
            else:
                data_list = [name for name in query]
                return data_list, cursor
        except Exception:
            return False
