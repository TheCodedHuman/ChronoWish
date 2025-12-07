from tkinter.ttk import Frame
from Utils.EntryField import EntryField


class InputSection:
    def __init__(self, parent: Frame):
        self.entryFrame = Frame(parent, padding=(0, 10))
        self.entryFrame.grid(sticky="we")
        self.entryFrame.columnconfigure(0, weight=1)
        self.entryFrame.columnconfigure(1, weight=1)

        # Name section
        self.nameField = EntryField(self.entryFrame, "Name", col=0)

        # UID section
        self.uidField = EntryField(self.entryFrame, "UID", col=1)
        
