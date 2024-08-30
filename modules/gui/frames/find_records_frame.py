from modules.db.db_connect import run_query
from modules.gui.table import column
from modules.gui.optionally.context_menu import show_context_menu
from tkinter import Menu


def find_records_frame(ttk, find_wind, tree, messagebox):
    def find_value():
        try:
            selected_column = selected_col.get()
            value = val.get()

            if selected_column:
                row_count = 0
                query = f"SELECT * FROM pfr WHERE \"{selected_column}\" LIKE '%{value}%'"
                result = run_query(query)
                for item in tree.get_children():
                    tree.delete(item)
                for row in result:
                    row_dict = dict(zip(column.keys(), row))
                    row_count += 1
                    if row_count % 2 == 0:
                        tree.insert('', 'end', values=tuple(row_dict.values()), tag='accent')
                    else:
                        tree.insert('', 'end', values=tuple(row_dict.values()))

        except Exception as e:
            messagebox.showerror("Ошибка!", e)

    col = ["СНИЛС", "ФИО Пенсионера", "Специалист ОВ", "№ Филиала", "Район", "Доставочная организация", "Очередность выплаты", "Выплатной месяц"]

    frame = ttk.LabelFrame(find_wind, text="Поиск", style="data.TLabelframe")
    frame.grid(row=0, column=2, rowspan=2, sticky='ns', pady=20, padx=20)

    ttk.Label(frame, text='Ввод ', style='data.TLabel').grid(row=1, column=0, pady=5)
    val = ttk.Entry(frame, width=20, font=20)
    val.grid(row=2, column=0, padx=10, pady=5)

    val.bind("<Button-3>", lambda event, entry=val: show_context_menu(find_wind, event, entry))

    ttk.Label(frame, text='Поиск по: ', style='data.TLabel').grid(row=1, column=1, pady=5)
    selected_col = ttk.Combobox(frame, values=col, width=18, font=20, state='readonly')
    selected_col.grid(row=2, column=1, pady=5)

    (ttk.Button(frame, text='Найти', command=find_value, style="data.TButton")
     .grid(row=3, column=0, columnspan=2, pady=5))