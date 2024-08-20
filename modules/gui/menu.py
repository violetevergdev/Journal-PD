from tkinter import Frame


# Создаем меню для основных кнопок
def menu(root, ttk, add_data, delete_data, edit_data):
    menu_frame = Frame(root)
    menu_frame.place(relx=0.009, rely=0.9, relwidth=0.98, relheight=0.09)

    ttk.Button(menu_frame, text='Добавить', command=add_data, style="btn.TButton").place(relx=0.01, rely=0.05,
                                                                                         relwidth=0.29, relheight=0.9)
    ttk.Button(menu_frame, text='Удалить', command=delete_data, style="btn.TButton").place(relx=0.355, rely=0.05,
                                                                                           relwidth=0.29, relheight=0.9)
    ttk.Button(menu_frame, text='Изменить', command=edit_data, style="btn.TButton").place(relx=0.7, rely=0.05,
                                                                                          relwidth=0.29, relheight=0.9)