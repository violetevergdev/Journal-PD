import re

from modules.gui.optionally.placeholder import placeholder


def fios_oper_period_entrys(ttk, frame, entry_font, show_context_menu):
    operations = ['Назначение', 'Постановка', 'Перерасчет']
    # ===========================================ФИО ПЕНСИОНЕРА====================================

    ttk.Label(frame, text='*ФИО Пенсионера: ', style='data.TLabel').grid(row=7, column=0, pady=5)
    fio_pens = ttk.Entry(frame, width=20, justify='center', foreground="gray", font=entry_font)
    placeholder("Фамилия И.О.", fio_pens)
    fio_pens.grid(row=7, column=1)

    fio_pens.bind("<Button-3>", lambda event, entry=fio_pens: show_context_menu(frame, event, entry))

    # ===========================================ОПЕРАЦИЯ====================================

    ttk.Label(frame, text='*Операция: ', style='data.TLabel').grid(row=8, column=0, pady=5)
    selected_operation = ttk.Combobox(frame, justify='center', values=operations, width=19, font=entry_font, state='readonly')
    selected_operation.grid(row=8, column=1)
    selected_operation.option_add('*TCombobox*Listbox.Justify', 'center')

    return fio_pens, selected_operation
