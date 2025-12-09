from tkinter.ttk import Frame
from .TempHoldLabel import TempHoldLabel

class SectionGroup2:
    def __init__(self, parent):
        self.groupFrame = Frame(parent)
        self.groupFrame.grid()

        # temporarily put temp hold lable to test dom manipulation
        TempHoldLabel(self.groupFrame)

