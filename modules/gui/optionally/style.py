

# Конфигурируем стиль
def style(styles):
    # ==============================Общие стили===============================

    styles.theme_use('clam')

    # Стили  для таблицы
    styles.configure('Treeview', font=0.2, rowheight='30')
    styles.configure('Treeview.Heading', font=0.2, background='#93a5a7')

    # Стили для полей
    styles.map('TCombobox', fieldbackground=[('readonly', 'white')], foreground=[('readonly', 'black')],
              selectbackground=[('readonly', '!focus', 'white')], selectforeground=[('readonly', '!focus', 'black')])
    styles.configure("TLabel", background="#93a5a7", font=5)

    # ==============================Опциональные стили===============================

    styles.configure("data.TLabelframe", background="#93a5a7", padding='10')
    styles.configure("data.TLabelframe.Label", background="#93a5a7", font=10, foreground="white")
    styles.configure("data.TButton", background="#93a5a7", font=10)

    styles.configure("err.TLabel", background="#93a5a7", font=10, foreground="red")

    styles.configure("table.TLabelframe", background="#f0f0f0")
    styles.configure("table.TLabelframe.Label", background="#f0f0f0", font=10)

    styles.configure("select.TButton", background="#dbdad5", padding='1', width="2", height="2")

    styles.configure("add.TButton", background="#93a5a7", padding='1')

    styles.configure("btn.TButton", font=12, background="#93a5a7")
