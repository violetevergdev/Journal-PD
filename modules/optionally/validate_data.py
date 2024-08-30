import re
from PyQt5.QtWidgets import QMessageBox


def show_error(self, message):
    QMessageBox.critical(self, "Ошибка ", message, QMessageBox.Ok)


def validate_data(self, data_entrys):
    sizes_data = [data_entrys[7], data_entrys[9], data_entrys[11]]
    non_empty_sizes = [el for el in sizes_data if el != ""]

    if not non_empty_sizes:
        show_error(self, "Укажите хотя бы один из размеров пенсии, ЕДВ или ДМО")
        return False

    for ind, v in enumerate(data_entrys):
        if ind in (7, 8, 9, 10, 11, 12, 15):
            continue
        elif v == "":
            show_error(self, "Заполните все обязательные поля! ")
            return False
        elif ind == 4:
            pattern = r"^\d{3}-\d{3}-\d{3} \d{2}$"
            if not re.match(pattern, v):
                show_error(self, "СНИЛС указан неверно!")
                return False
        elif ind == 5:
            fio_good_pattern = r"^[А-ЯЁ][а-яё]+ [А-ЯЁ]\.[А-ЯЁ]\.$"
            fio_error_pattern = r"^[А-ЯЁа-яё]+ [А-ЯЁ]\.{0,1}[А-ЯЁ]\.{0,1}$"

            if v == '':
                show_error(self, "Ошибка! Укажите ФИО Пенсионера")
                return False

            if not re.match(fio_good_pattern, v):
                if re.match(fio_error_pattern, v):
                    fio_parts = v.split()
                    if len(fio_parts) == 2:
                        surname, initials = fio_parts
                        surname = surname.capitalize()

                        formatted_initials = ""
                        for char in initials:
                            if char.isalpha():
                                formatted_initials += char + "."

                        formatted_fio = f"{surname} {formatted_initials}"
                        self.ui_window.fio_pens.setText("")
                        self.ui_window.fio_pens.setText(formatted_fio)
                        data_entrys[5] = formatted_fio


                else:
                    show_error(self, "Ошибка! Неверный формат ФИО!")
                    return False

    return True
