from tkinter import ttk
from tkinter import Tk, messagebox, Toplevel, Menu
from tkinter.simpledialog import askstring

from modules.gui.optionally.style import style
from modules.gui.frames.data_frame import data_frame
from modules.gui.table import table
from modules.gui.menu import menu
from modules.db.db_connect import run_query
from modules.gui.table import get_records
from modules.gui.frames.find_records_frame import find_records_frame
from modules.db.unload_data import unload_data


def gui():
    CP = '4525'

    # Очищаем наш select
    def clear_select(event):
        item = tree.identify('item', event.x, event.y)
        if not item:
            tree.selection_set('')

    # Обработка добавления записи
    def add_data():
        add_wind = Toplevel()
        add_wind.configure(bg="#93a5a7")
        add_wind.resizable(width=False, height=False)
        data_frame(add_wind, ttk, tree, type_event="ADD")
        add_wind.protocol("WM_DELETE_WINDOW", lambda: add_wind.destroy())
        add_wind.mainloop()

    # Обработка удаления записи
    def delete_data():
        try:
            selected_item = tree.selection()
            if selected_item:
                el = tree.item(selected_item)['values'][0]
                password_entry = askstring('Подтверждение', 'Ведите пароль', parent=root)
                if password_entry == CP:
                    try:
                        query = 'DELETE FROM pfr WHERE id = ?'
                        run_query(query, (el,))
                        get_records(tree)
                        messagebox.showinfo("Успех", "Запись была успешно удалена!")
                    except Exception as e:
                        messagebox.showerror("Ошибка", "Не удалось удалить выбранную запись")
                else:
                    messagebox.showerror("Ошибка", "Неверный пароль")
            else:
                messagebox.showerror("Ошибка", "Выберите запись для удаления")
        except Exception as e:
            messagebox.showinfo("Ошибка!", "Непредвиденная ошибка" + str(e))

    # Обработка редактирования записи
    def edit_data():
        try:
            selected_item = tree.selection()
            if selected_item:
                el = tree.item(selected_item)['values']
                edit_wind = Toplevel()
                edit_wind.configure(bg="#93a5a7")
                edit_wind.resizable(width=False, height=False)
                err = data_frame(edit_wind, ttk, tree, type_event="EDIT", existing_values=el)
                if err:
                    messagebox.showerror("Ошибка!", "Ошибка изменения записи" + str(err))

                edit_wind.protocol("WM_DELETE_WINDOW", lambda: edit_wind.destroy())

                edit_wind.mainloop()
            else:
                messagebox.showerror("Ошибка", "Выберите запись для редактирования")
        except Exception as e:
            messagebox.showinfo("Ошибка!", "Непредвиденная ошибка" + str(e))

    # Обработка поиска записей
    def find_record():
        find_wind = Toplevel()
        find_wind.configure(bg="#93a5a7")
        find_wind.resizable(width=False, height=False)
        find_records_frame(ttk, find_wind, tree, messagebox)
        find_wind.protocol("WM_DELETE_WINDOW", lambda: find_wind.destroy())
        find_wind.mainloop()

    root = Tk()
    root.title("Журнал ПД")
    root.geometry("1400x800")

    main_menu = Menu()
    main_menu.add_cascade(label="Выгрузить", command=unload_data)
    main_menu.add_cascade(label="Обновить", command=lambda: get_records(tree))
    main_menu.add_cascade(label="Поиск", command=find_record)

    root.config(menu=main_menu)

    style(ttk.Style())

    tree = table(root, ttk)

    menu(root, ttk, add_data, delete_data, edit_data)

    root.bind("<Button-3>", clear_select)
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

    root.mainloop()


if __name__ == "__main__":
    gui()
