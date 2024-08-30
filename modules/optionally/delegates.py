from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtCore import Qt

class TableItemDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(TableItemDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

    def displayText(self, value, locale):
        if isinstance(value, float):
            return "{:.2f}".format(value)
        return super().displayText(value, locale)
