from modules.gui.optionally.placeholder import placeholder


def snils_entry(ttk, frame, entry_font, entry_width, root, show_context_menu):

    def validate_snils(new_num):
        if any(c not in '0123456789_- ' for c in new_num):
            return False

        max_length = 14

        return len(new_num) <= max_length

    ttk.Label(frame, text='*СНИЛС: ', style='data.TLabel').grid(row=6, column=0, pady=5)

    snils = ttk.Entry(frame, width=entry_width, justify='center', foreground="gray", font=entry_font,
                      validate='all', validatecommand=(root.register(validate_snils), '%P'))

    placeholder('___-___-___ __', snils)

    snils.grid(row=6, column=1)

    snils.bind("<Button-3>", lambda event, entry=snils: show_context_menu(frame, event, entry))

    return snils

