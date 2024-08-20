import re


def district_entry(ttk, frame, entry_font, root):
    def validate_district(P):
        if len(P) <= 3 and re.match(r"^\d*$", P):
            return True
        return False

    ttk.Label(frame, text='*Район: ', style='data.TLabel').grid(row=5, column=0, pady=5)
    district = ttk.Entry(frame, width=5, justify='center', font=entry_font,
                         validate="all", validatecommand=(root.register(validate_district), '%P'))
    district.grid(row=5, column=1, pady=10)

    return district
