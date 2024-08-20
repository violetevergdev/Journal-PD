

def sizes_allowance_entrys(ttk, frame, entry_font, root):
    frame_size = ttk.LabelFrame(frame, style="data.TLabelframe")

    frame_size.grid(row=13, column=0, sticky='ns', columnspan=2, pady=10, padx=10)

    # ===========================================УСТ.Размер ПЕНС====================================

    def validate_size_allowance(new_num):
        if any(c not in '0123456789.,' for c in new_num):
            return False
        else:
            return True

    vmcd = root.register(validate_size_allowance), '%P'

    ttk.Label(frame_size, text='УСТ. Размер Пенсии: ', style='data.TLabel').grid(row=1, column=0, pady=5)
    set_size_pens = ttk.Entry(frame_size, justify='center', width=10,
                              validate='all',
                              validatecommand=vmcd,
                              font=entry_font)
    set_size_pens.grid(row=2, column=0)

    # ===========================================Доплата ПЕНС====================================

    ttk.Label(frame_size, text='Доплата Пенсии: ', style='data.TLabel').grid(row=1, column=1, pady=5)
    allowance_pens = ttk.Entry(frame_size, justify='center', width=10,
                               validate='all',
                               validatecommand=vmcd,
                               font=entry_font)
    allowance_pens.grid(row=2, column=1)

    # ===========================================УСТ.Размер ЕДВ====================================

    ttk.Label(frame_size, text='УСТ.Размер ЕДВ: ', style='data.TLabel').grid(row=3, column=0, pady=5)
    set_size_edv = ttk.Entry(frame_size, font=entry_font, justify='center', validate='all', width=10,
                             validatecommand=vmcd)
    set_size_edv.grid(row=4, column=0)

    # ===========================================Доплата ЕДВ====================================

    ttk.Label(frame_size, text='Доплата ЕДВ: ', style='data.TLabel').grid(row=3, column=1, pady=5)
    allowance_edv = ttk.Entry(frame_size, font=entry_font, justify='center', width=10,
                              validate='all',
                              validatecommand=vmcd)
    allowance_edv.grid(row=4, column=1)

    # ===========================================УСТ.Размер ДМО====================================

    ttk.Label(frame_size, text='УСТ.Размер ДМО: ', style='data.TLabel').grid(row=5, column=0, pady=5)
    set_size_dmo = ttk.Entry(frame_size, font=entry_font, validate='all', justify='center', width=10,
                             validatecommand=vmcd)
    set_size_dmo.grid(row=6, column=0)

    # ===========================================Доплата ДМО====================================

    ttk.Label(frame_size, text='Доплата ДМО: ', style='data.TLabel').grid(row=5, column=1, pady=5)
    allowance_dmo = ttk.Entry(frame_size, font=entry_font, validate='all', justify='center', width=10,
                              validatecommand=vmcd)
    allowance_dmo.grid(row=6, column=1)

    return (set_size_pens, allowance_pens, set_size_edv,
            allowance_edv, set_size_dmo, allowance_dmo)