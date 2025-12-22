from tkinter.ttk import Frame, Treeview, Scrollbar

class IntelTable:
    
    def __init__(self, parent, columns: list[str]):

        # Frame wrapping Table and Scrollbar
        self.IntelFrame = Frame(parent)
        self.IntelFrame.grid(sticky="news")
        self.IntelFrame.columnconfigure(0, weight=1)
        self.IntelFrame.rowconfigure(0, weight=1)

        # Treeview birthday table
        self.birthdayTable = Treeview(self.IntelFrame, columns=columns, height=5, show="headings")
        self.birthdayTable.grid(sticky="we")

        # Table's scrollbar
        scrollbar = Scrollbar(self.IntelFrame, orient="vertical", command=self.birthdayTable.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        for col in columns:
            self.birthdayTable.heading(col, text=col)
            self.birthdayTable.column(col, anchor="center")

    
    def update_table(self, rows: list[tuple | list]):
        """Clears the data in table, and inserts the new data"""

        # Clear/Delete data/rows
        for item in self.birthdayTable.get_children():
            self.birthdayTable.delete(item)

        # Insert new data
        for row in rows:
            self.birthdayTable.insert("","end", values=row)

