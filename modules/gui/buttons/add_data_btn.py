import re
from tkinter import messagebox

from modules.db.db_connect import run_query
from modules.gui.table import get_records


# Обработка добавления записи в БД
def add_data_btn(ttk, root, frame, data_entrys, error, tree, type_event, id_el=None):
    def get_parameters():
        param = []

        for v in data_entrys.values():
            data = v.get()
            param.append(data)

        return param

    def validate_data():
        non_empty_sizes = [data_entrys[key] for key in ['set_size_pens', 'set_size_edv', 'set_size_dmo'] if
                                              data_entrys[key].get() != ""]
        if not non_empty_sizes:
           error.config(text="Ошибка! Укажите хотя бы один\nиз размеров пенсии, ЕДВ или ДМО")
           return False

        for k, v in data_entrys.items():
            if k == 'Примечание' or any(c in 'sa' for c in k):
                continue
            elif v.get() == "":
                error.config(text="Ошибка! Укажите " + k)
                return False
            elif k == 'СНИЛС':
                pattern = r"^\d{3}-\d{3}-\d{3} \d{2}$"
                if not re.match(pattern, v.get()):
                    error.config(text="Ошибка! СНИЛС указан неверно!")
                    return False
            elif k == 'ФИО Пенсионера':
                fio_good_pattern = r"^[А-ЯЁ][а-яё]+ [А-ЯЁ]\.[А-ЯЁ]\.$"
                fio_error_pattern = r"^[А-ЯЁа-яё]+ [А-ЯЁ]\.{0,1}[А-ЯЁ]\.{0,1}$"

                if v.get() == 'Фамилия И.О.':
                    error.config(text="Ошибка! Укажите " + k)
                    return False

                if not re.match(fio_good_pattern, v.get()):
                    if re.match(fio_error_pattern, v.get()):
                        fio_parts = v.get().split()
                        if len(fio_parts) == 2:
                            surname, initials = fio_parts
                            surname = surname.capitalize()

                            formatted_initials = ""
                            for char in initials:
                                if char.isalpha():
                                    formatted_initials += char + "."

                            formatted_fio = f"{surname} {formatted_initials}"
                            v.delete(0, 'end')
                            v.insert(0, formatted_fio)

                    else:
                        error.config(text="Ошибка! Неверный формат ФИО!")
                        return False

        return True

    def clear_form():
        for k, v in data_entrys.items():
            if k in ('№ Филиала', 'ОПЕРАЦИЮ'):
                v.set("")
            elif k == 'Дост. организация':
                v.config(state='normal')
                v.delete(0, 'end')
                v.config(state='readonly')
            elif k == 'СНИЛС':
                v.delete(0, 'end')
                v.insert(0, "___-___-___ __")
                v.configure(foreground="gray")
            elif k == 'ФИО Пенсионера':
                v.delete(0, 'end')
                v.insert(0, "Фамилия И.О.")
                v.configure(foreground="gray")
            elif k == 'Специалиста ОВ':
                continue
            else:
                v.delete(0, 'end')

    def push_data():
        try:
            error.config(text="")
            if validate_data():
                if type_event == 'ADD':
                    query = 'INSERT INTO pfr VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                elif type_event == 'EDIT':
                    query = f'''UPDATE pfr SET 'Очередность выплаты' = ?, 'Выплатной месяц' = ?, '№ Филиала' = ?,
                     Район = ?, СНИЛС = ?, 'ФИО Пенсионера' = ?, Операция = ?, 'УСТ. Размер пенсии' = ?, 
                     'Доплата ПЕНС' = ?, 'УСТ. Размер ЕДВ' = ?, 'Доплата ЕДВ' = ?, 'УСТ. Размер ДМО' = ?, 
                    'Доплата ДМО' = ?, 'Доставочная организация' = ?, 'Специалист ОВ' = ?, Примечание = ?, 'Дата отработки' = ? 
                    WHERE id = {id_el}'''
                parameters = get_parameters()
                run_query(query, parameters)
                if type_event == 'ADD':
                    clear_form()
                elif type_event == 'EDIT':
                    messagebox.showinfo("Успех!", "Запись была успешно изменена!")
                    root.destroy()
            get_records(tree)
        except Exception as e:
            if type_event == 'ADD':
                error.config(text="Ошибка добавления новой записи\n" + str(e))
            else:
                error.config(text="Ошибка изменения записи\n" + str(e))

    ttk.Button(frame, text='Сохранить', style="data.TButton", command=push_data).grid(row=14, columnspan=2, sticky='we', pady=5)
