from tkinter.ttk import Frame
from .InputSection import InputSection
from .DateSelectSection import DateSelectSection
from .MainButtons import ResetButton, SubmitButton

class SectionGroup1:
    def __init__(self, parent: Frame):
        self.groupFrame = Frame(parent)
        self.groupFrame.grid()

        # Input Section
        self.entries = InputSection(self.groupFrame)

        # Date-Select Section
        self.date = DateSelectSection(self.groupFrame)

        # ButtonFrame Section
        self.fields = [self.entries, self.date]                 # each field is providing 2 values currently

        self.buttons = Frame(self.groupFrame, padding=(0, 10))
        self.buttons.grid()

        ResetButton(self.buttons, resetFields=self.fields)
        self.submitButton = SubmitButton(self.buttons, submitFields=self.fields)
        
    