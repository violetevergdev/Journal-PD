from PyQt5.QtWidgets import QFileDialog

import os
import pandas as pd
from datetime import datetime


def unload_XLSX_data(data, cursor):

    # Получаем DataFrame
    results = pd.DataFrame(data, columns=[col[0] for col in cursor.description])

    # Запрашиваем выходной путь
    out_dir = str(QFileDialog.getExistingDirectory(None, "Выберите каталог"))

    # Устанавливаем выходной путь
    out = os.path.join(out_dir, f'Журнал ПД Выгрузка от {datetime.today().date()}.xlsx')

    # Записываем данные
    writer = pd.ExcelWriter(out)
    results.to_excel(writer, index=False)

    writer.close()
