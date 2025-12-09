from tkinter.ttk import Frame
from Utils.EntryField import EntryField

class InputSection:
    def __init__(self, parent: Frame):
        self.entryFrame = Frame(parent, padding=(0, 10))
        self.entryFrame.grid()

        # Name section
        self.nameField = EntryField(self.entryFrame, "Name", col=0)

        # UID section
        self.uidField = EntryField(self.entryFrame, "UID", col=1)
        
    
    def get(self):
        return {
            "name": self.nameField.get(),
            "uid": self.uidField.get()
        }
    
    def clear(self):
        self.nameField.clear()
        self.uidField.clear()
    
