from tkinter.ttk import Frame
from ..SectionGroup2.TempHoldLabel import TempHoldLabel

class SectionGroup3:
    def __init__(self, parent):
        self.groupFrame = Frame(parent)
        self.groupFrame.grid()

        # temporarily put temp hold lable to test dom manipulation
        TempHoldLabel(self.groupFrame)

