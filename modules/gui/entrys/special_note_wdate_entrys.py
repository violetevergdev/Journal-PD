from tkcalendar import DateEntry


def note_wdate_entrys(ttk, frame, entry_font):

    # ==========================================Специалист О.В.====================================

    ttk.Label(frame, text='*Специалист О.В.: ', style='data.TLabel').grid(row=10, column=0, pady=5)
    selectd_specialist = ttk.Entry(frame,justify='center', width=20, font=entry_font)
    selectd_specialist.grid(row=10, column=1)
    selectd_specialist.option_add('*TCombobox*Listbox.Justify', 'center')

    # ===========================================Примечание====================================

    ttk.Label(frame, text='Примечание: ', style='data.TLabel').grid(row=11, column=0, pady=5)
    note = ttk.Entry(frame, width=20, justify='center',  font=entry_font, background='#D3D3D3')
    note.grid(row=11, column=1)

    # ===========================================Дата Отработки====================================

    ttk.Label(frame, text='*Дата отработки: ', style='data.TLabel').grid(row=12, column=0, pady=5)
    workout_date = DateEntry(frame, locale='ru_RU', justify='center', firstweekday="monday", font=entry_font, state='readonly')
    workout_date.grid(row=12, column=1)

    return selectd_specialist, note, workout_date
