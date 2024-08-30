
create_pfr_db = ('''
            CREATE TABLE IF NOT EXISTS pfr (
                id INTEGER PRIMARY KEY,
                'Очередность выплаты' text NOT NULL,
                'Выплатной месяц' text NOT NULL,
                '№ Филиала' text NOT NULL,
                Район INTEGER NOT NULL,
                СНИЛС text NOT NULL,
                'ФИО Пенсионера' text NOT NULL,
                Операция text NOT NULL,
                'УСТ Размер пенсии' float,
                'Доплата ПЕНС' float,
                'УСТ Размер ЕДВ' float,
                'Доплата ЕДВ' float,
                'УСТ Размер ДМО' float,
                'Доплата ДМО' float,
                'Доставочная организация' text NOT NULL,
                'Специалист ОВ' text NOT NULL,
                Примечание text,
                'Дата отработки' datetime NOT NULL
            )
            ''')

create_bank_db=('''
    CREATE TABLE IF NOT EXISTS banks (
        Наименование text NOT NULL UNIQUE
    )
''')


