from modules.gui.optionally.context_menu import show_context_menu
from modules.db.db_connect import run_query
from modules.gui.entrys.district_entry import district_entry
from modules.gui.entrys.snils_entry import snils_entry
from modules.gui.entrys.fios_oper_period_entrys import fios_oper_period_entrys
from modules.gui.entrys.sizes_allowance_entrys import sizes_allowance_entrys
from modules.gui.entrys.priority_mounth_filial_frames import priority_mounth_filial_frames
from modules.gui.entrys.bank_entry import bank_entry
from modules.gui.entrys.special_note_wdate_entrys import note_wdate_entrys
from modules.gui.buttons.add_data_btn import add_data_btn


entry_width = 15
entry_font = 20


def get_banks():
    query_bank = 'SELECT * FROM banks'
    result_bank = run_query(query_bank)
    banks_list = [name[0].title() for name in result_bank]
    return banks_list

# ===============Настройка фрейма добавляения новых записей=======================


def data_frame(root, ttk, tree, type_event="ADD", existing_values=None):
    banks = get_banks()

    if type_event == "ADD":
        label_name = 'Новая запись'
    elif type_event == "EDIT":
        label_name = 'Редактор записи'

    frame = ttk.LabelFrame(root, text=label_name, style="data.TLabelframe")

    frame.grid(row=0, column=2, rowspan=2, sticky='ns', pady=20, padx=20)

    error_label = ttk.Label(frame, text="", style="err.TLabel")
    error_label.grid(row=1, column=0, columnspan=2)

    # ================Очередность выплаты, Выплатной месяц, № Филиала====================================
    payment_priority, pay_month, num_of_filial = priority_mounth_filial_frames(ttk, frame, entry_font)
    # ================Район====================================
    district = district_entry(ttk, frame, entry_font, root)
    # # ================СНИЛС====================================
    snils = snils_entry(ttk, frame, entry_font, entry_width, root, show_context_menu)
    # # ===========ФИО, ОПЕРАЦИЯ ===========================
    fio_pens, operation = fios_oper_period_entrys(ttk, frame, entry_font, show_context_menu)
    # =======================БАНК===========================
    bank = bank_entry(ttk, frame, entry_font, banks)
    #  ====Специалист, Примечание, Дата Отработки==========================
    specialist, note, wdate = note_wdate_entrys(ttk, frame, entry_font)
    # ============УСТ.Размеры====================================
    values = sizes_allowance_entrys(ttk, frame, entry_font, root, show_context_menu)

    # ===========================================КНОПКА ОБРАБОТКИ====================================
    data_entrys = {
        'Очередность выплаты': payment_priority,
        'Выплатной месяц': pay_month,
        '№ Филиала': num_of_filial,
        'Район': district,
        'СНИЛС': snils,
        'ФИО Пенсионера': fio_pens,
        'ОПЕРАЦИЮ': operation,
        'set_size_pens': values[0],
        'allowance_pens': values[1],
        'set_size_edv': values[2],
        'allowance_edv': values[3],
        'set_size_dmo': values[4],
        'allowance_dmo': values[5],
        'Дост. организация': bank,
        'Специалиста ОВ': specialist,
        'Примечание': note,
        'Дата Отработки': wdate,
    }
    if type_event == "ADD":
        id_el=""

    if existing_values:
        id_el = existing_values[0]
        for el, val in zip(existing_values[1:], data_entrys.items()):
            if val[0] in ('Очередность выплаты', 'Выплатной месяц', '№ Филиала', 'ОПЕРАЦИЮ'):
                val[1].set(el)
            elif val[0] == 'Дост. организация':
                val[1].config(state='normal')
                val[1].insert(0, el)
                val[1].config(state='readonly')
            elif val[0] in ('СНИЛС', 'ФИО Пенсионера'):
                val[1].delete(0, 'end')
                val[1].insert(0, el)
                val[1].configure(foreground="black")
            elif val[0] == 'Дата Отработки':
                val[1].set_date(el)
            else:
                val[1].insert(0, el)

    add_data_btn(ttk, root, frame, data_entrys, error_label, tree, type_event, id_el)
