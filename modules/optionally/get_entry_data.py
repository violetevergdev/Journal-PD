

def get_entry_data(self):
    data_entrys = list()

    payment_priority = self.ui_window.priority.currentText()
    data_entrys.append(payment_priority)

    pay_month = self.ui_window.month.currentText()
    data_entrys.append(pay_month)

    num_of_filial = self.ui_window.filial.currentText()
    data_entrys.append(num_of_filial)

    district = self.ui_window.district.text()
    data_entrys.append(district)

    snils = self.ui_window.snils.text()
    data_entrys.append(snils)

    fio_pens = self.ui_window.fio_pens.text()
    data_entrys.append(fio_pens)

    operation = self.ui_window.operation_type.currentText()
    data_entrys.append(operation)

    size_Pens = self.ui_window.size_Pens.text()
    data_entrys.append(size_Pens)

    allow_Pens = self.ui_window.allow_Pens.text()
    data_entrys.append(allow_Pens)

    size_EDV = self.ui_window.size_EDV.text()
    data_entrys.append(size_EDV)

    allow_EDV = self.ui_window.allow_EDV.text()
    data_entrys.append(allow_EDV)

    size_DMO = self.ui_window.size_DMO.text()
    data_entrys.append(size_DMO)

    allow_DMO = self.ui_window.allow_DMO.text()
    data_entrys.append(allow_DMO)

    bank = self.ui_window.bank.text()
    data_entrys.append(bank)

    specialist = self.ui_window.specialist.text()
    data_entrys.append(specialist)

    note = self.ui_window.note.text()
    data_entrys.append(note)

    wdate = self.ui_window.wdate.text()
    data_entrys.append(wdate)

    return data_entrys