from tkinter.ttk import Frame
from Utils.IntelTable import IntelTable
from Utils.chrono_utils import ReorderBirthdayData

class ResultSection:
    def __init__(self, parent):

        self.resultFrame = Frame(parent)
        self.resultFrame.grid(sticky="we")

        # Intel-Table
        self.col_order = ("Age", "DOB", "Name", "UID")              # for 4 columns there can be 24 possible combinations 4!
        self.birthdayTable = IntelTable(self.resultFrame, columns=self.col_order)     


    def update_results(self, rows: list[tuple]):            # this recieves the list[tuple] that isn't processed yet
        reorder_util: object = ReorderBirthdayData(rows, self.col_order, debug=True)
        processed_rows = reorder_util.reorder_data()
        self.birthdayTable.update_table(processed_rows)               # this doesn't care if its processed or not, it should just get its rows: list[tuple | list]

