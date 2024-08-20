
def priority_mounth_filial_frames(ttk, frame, entry_font):

    # ================Очередность выплаты====================================
    priority = ['Основная', 'Разовая', 'Доп.  1', 'Доп. 2', 'Доп. 3']

    ttk.Label(frame, text='*Очередность выплаты: ', style='data.TLabel').grid(row=2, column=0, pady=5)
    payment_priority = ttk.Combobox(frame, values=priority, justify='center', width=15, font=entry_font,
                                    state='readonly')
    payment_priority.grid(row=2, column=1)
    payment_priority.option_add('*TCombobox*Listbox.Justify', 'center')

    # ================Выплатной месяц====================================
    month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
             'Ноябрь', 'Декабрь']

    ttk.Label(frame, text='*Выплатной месяц: ', style='data.TLabel').grid(row=3, column=0, pady=5)
    pay_month = ttk.Combobox(frame, values=month, justify='center', width=15, font=entry_font, state='readonly')
    pay_month.grid(row=3, column=1)
    pay_month.option_add('*TCombobox*Listbox.Justify', 'center')

    # ================№ Филиала====================================
    filial = ['Ф-л 1', 'Ф-л 2', 'Ф-л 3', 'Ф-л 4', 'Ф-л 5', 'Ф-л 6', 'Ф-л 7', 'Ф-л 8', 'Ф-л 9', 'Ф-л 10']

    ttk.Label(frame, text='*№ Филиала: ', style='data.TLabel').grid(row=4, column=0, pady=5)
    num_of_filial = ttk.Combobox(frame, values=filial, justify='center', width=15, font=entry_font, state='readonly')
    num_of_filial.grid(row=4, column=1)
    num_of_filial.option_add('*TCombobox*Listbox.Justify', 'center')

    return payment_priority, pay_month, num_of_filial