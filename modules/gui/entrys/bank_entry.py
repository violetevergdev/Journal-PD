from tkinter import simpledialog, messagebox, Toplevel, Variable, Listbox
from modules.db.db_connect import run_query


def bank_entry(ttk, frame, entry_font, bank_data):
    frame_bank = ttk.Frame(frame)
    frame_bank.grid(row=9, column=1)

    ttk.Label(frame, text='*Банк: ', style='data.TLabel').grid(row=9, column=0, pady=5)
    selected_bank = ttk.Entry(frame_bank, width=18, justify='center', font=entry_font, state='readonly')
    selected_bank.grid(row=1, column=0)

    select_btn = ttk.Button(frame_bank, text='+', style="select.TButton", command=lambda: show_bank_list(bank_data)).grid(
        row=1, column=1)

    # Обработка выбора банка из БД
    def show_bank_list(values):
        def select_bank(bank_name):
            selected_bank.config(state='normal')
            selected_bank.delete(0, 'end')
            selected_bank.insert(0, bank_name)
            selected_bank.config(state='readonly')
            list_wind.destroy()

        # Обработка добавления банка в БД
        def add_bank():
            new_bank = simpledialog.askstring("Новый банк", "Введите название банка:")
            if new_bank:
                try:
                    query = 'INSERT INTO banks VALUES (?)'
                    run_query(query, (new_bank,))

                    values.append(new_bank)
                    items.set(values)
                except Exception as e:
                    messagebox.showerror("Ошибка!", "Такой банк уже существует!" + str(e))
                    frame.focus()
                    list_wind.focus()

        # Добавление фрейма для отображения списка банков
        list_wind = Toplevel()
        list_wind.configure(bg="#93a5a7")

        search_frame = ttk.LabelFrame(list_wind, text="Поиск", style='data.TLabelframe')
        search_frame.grid(row=0, column=0)

        search_entry = ttk.Entry(search_frame, font=entry_font)
        search_entry.grid(row=1, column=0, pady=15)

        add_button = ttk.Button(search_frame, text="Добавить", style="add.TButton", command=add_bank)
        add_button.grid(row=1, column=1)

        values = [value.upper() for value in values]

        items = Variable(value=values)
        lst = Listbox(list_wind, listvariable=items, font=entry_font, width=40, height=20, justify='center',
                         bg='#bec9ca')
        lst.grid(row=1, column=0)

        # Обработка поиска банка в списке
        def filter_list(event):
            search_term = search_entry.get().lower()
            filtered_items = [item for item in values if search_term in item.lower()]
            items.set(filtered_items)

        search_entry.bind('<KeyRelease>', filter_list)
        lst.bind('<Double-1>', lambda event: select_bank(lst.get(lst.curselection())))

        list_wind.protocol("WM_DELETE_WINDOW", lambda: list_wind.destroy())
        list_wind.mainloop()

    return selected_bank

