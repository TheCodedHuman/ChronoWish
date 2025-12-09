from tkinter.ttk import Frame, Label

class TempHoldLabel:
    def __init__(self, parent):
        self.tempFrame = Frame(parent)
        self.tempFrame.grid()
        self.tempFrame.columnconfigure(0, weight=1)

        # Temp Label
        Label(self.tempFrame, text="Coming Soon...").grid(sticky="news")

