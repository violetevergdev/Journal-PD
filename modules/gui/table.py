from modules.gui.optionally.get_records import column, get_records


def table(root, ttk,):
    # Прокрутка по вертикали при прокрутке колеса мыши
    def on_mousewheel(event):
        tree.yview_scroll(-5 * int(event.delta / 120), "units")

    # Создаем фрейм для таблицы
    table_frame = ttk.LabelFrame(root, text='Журнал пенсионных дел', style='table.TLabelframe')
    table_frame.place(relx=0.009, rely=0.01, relwidth=0.98, relheight=0.88)

    # Получаем столбцы
    col = tuple(column.values())

    tree = ttk.Treeview(table_frame, columns=col, show='headings')

    # Создаем заголовки
    for c in col:
        tree.heading(c, text=c, anchor='center')

    # Настройка столбцов
    tree.column('#1', width=55, stretch=False, minwidth=15, anchor='center')
    tree.column('#2', width=190, stretch=False, minwidth=30, anchor='center')
    tree.column('#3', width=170, stretch=False, minwidth=50, anchor='center')
    tree.column('#4', width=100, stretch=False, minwidth=50, anchor='center')
    tree.column('#5', width=80, stretch=False, minwidth=50, anchor='center')
    tree.column('#6', width=170, stretch=False, minwidth=50, anchor='center')
    tree.column('#7', width=190, stretch=False, minwidth=50, anchor='center')
    tree.column('#8', width=170, stretch=False, minwidth=50, anchor='center')
    tree.column('#9', width=120, stretch=False, minwidth=50, anchor='center')
    tree.column('#10', width=120, stretch=False, minwidth=50, anchor='center')
    tree.column('#11', width=120, stretch=False, minwidth=50, anchor='center')
    tree.column('#12', width=120, stretch=False, minwidth=50, anchor='center')
    tree.column('#13', width=120, stretch=False, minwidth=50, anchor='center')
    tree.column('#14', width=120, stretch=False, minwidth=50, anchor='center')
    tree.column('#15', width=190, stretch=False, minwidth=50, anchor='center')
    tree.column('#16', width=190, stretch=False, minwidth=50, anchor='center')
    tree.column('#17', width=140, stretch=False, minwidth=50, anchor='center')
    tree.column('#18', width=140, stretch=False, minwidth=50, anchor='center')

    tree.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Размещаем скроллбары
    scrollbarx_frame = ttk.Frame(table_frame)
    scrollbarx_frame.place(relx=0.05, rely=0.97, relwidth=0.9)

    scrollbarx = ttk.Scrollbar(scrollbarx_frame, orient='horizontal', command=tree.xview)
    scrollbarx.pack(fill="x")

    scrollbary_frame = ttk.Frame(table_frame)
    scrollbary_frame.place(relx=0.993, rely=0.06, relwidth=0.007, relheight=0.9)

    scrollbary = ttk.Scrollbar(scrollbary_frame, orient='vertical', command=tree.yview)
    scrollbary.pack(fill="y", side="right")

    tree.configure(xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

    # Получаем данные из БД и отображаем ее в tree
    get_records(tree)

    # Добавляем обработку события для скролла
    tree.bind_all("<MouseWheel>", on_mousewheel)

    return tree
