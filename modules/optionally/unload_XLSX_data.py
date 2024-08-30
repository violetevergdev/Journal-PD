from PyQt5.QtWidgets import QFileDialog, QMessageBox

import os
import sqlite3
import pandas as pd
from datetime import datetime


def unload_XLSX_data():
    # with sqlite3.connect('pfr.db') as conn:
    with sqlite3.connect('W:\\!VIOLETTA!\\!fw!\\journal\\journal.db') as conn:
        cursor = conn.cursor()

    query = cursor.execute('SELECT * FROM pfr')

    # Получаем DataFrame
    results = pd.DataFrame(query, columns=[col[0] for col in cursor.description])

    # Запрашиваем выходной путь
    out_dir = str(QFileDialog.getExistingDirectory(None, "Выберите каталог"))

    # Устанавливаем выходной путь
    out = os.path.join(out_dir, f'Журнал ПД Выгрузка от {datetime.today().date()}.xlsx')

    # Записываем данные
    writer = pd.ExcelWriter(out)
    results.to_excel(writer, index=False)

    writer.close()

    QMessageBox.information(None, "Выгрузка в XLSX", "Данные успешно выгружены")