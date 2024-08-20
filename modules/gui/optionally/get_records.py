from modules.db.db_connect import run_query


column = {
    0: 'ID',
    1: 'Очередность выплаты',
    2: 'Выплатной месяц',
    3: '№ Филиала',
    4: 'Район',
    5: 'СНИЛС',
    6: 'ФИО Пенсионера',
    7: 'Операция',
    8: 'УСТ ПЕНС',
    9: 'Доплата ПЕНС',
    10: 'УСТ ЕДВ',
    11: 'Доплата ЕДВ',
    12: 'УСТ ДМО',
    13: 'Доплата ДМО',
    14: 'Банк',
    15: 'Специалист ОВ',
    16: 'Примечание',
    17: 'Дата отработки'
}


# заполнение таблицы данными
def get_records(tree):
    row_count = 0
    records = tree.get_children()
    for element in records:
        tree.delete(element)

    query = 'SELECT * FROM pfr ORDER BY ID'
    db_rows = run_query(query)

    for row in db_rows:
        row_dict = dict(zip(column.keys(), row))
        row_val = tuple(row_dict.values())
        row_count += 1
        if row_count % 2 == 0:
            tree.insert('', 'end', values=row_val, tag='accent')
        else:
            tree.insert('', 'end', values=row_val)

    tree.tag_configure('accent', background='#bec9ca')
