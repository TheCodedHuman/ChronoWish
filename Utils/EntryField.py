from tkinter import StringVar
from tkinter.ttk import Frame, Entry, Label


class EntryField:
    def __init__(self, parent: Frame, label: str, col: int):

        # Frame containing Label and Entry together
        self.instanceFrame = Frame(parent, padding=(0, 10))
        self.instanceFrame.grid(row=0, column=col, sticky="we", padx=10)

        # EntryLabel
        self.label = label + ":"
        Label(self.instanceFrame, text=self.label).grid(row=0, column=0, sticky="e", padx=3)

        # EntryField
        self.instanceEntryField = StringVar()
        self.entry = Entry(self.instanceFrame, width=30, textvariable=self.instanceEntryField)
        self.entry.grid(row=0, column=1, sticky="w")


    # DeBug-able Get method
    def get(self, debug: bool = False) -> str:
        if debug:
            print(self.instanceEntryField.get())
            return self.instanceEntryField.get()
        else:
            return self.instanceEntryField.get()


    def clear(self):
        self.instanceEntryField.set("")

