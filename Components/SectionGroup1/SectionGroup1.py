from tkinter.ttk import Frame
from .InputSection import InputSection
from .DateSelectSection import DateSelectSection
from .MainButtons import ResetButton, SubmitButton
from .ResultSection import ResultSection

# SubmitButton → collects fields → fetches DB → returns result
# ResultSection → receives result → updates IntelTable

class SectionGroup1:
    def __init__(self, parent: Frame, db):
        self._db = db
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

        # Intel Table and ProgressBar Section
        self.resultSection = ResultSection(self.groupFrame)     # had to call earlier due to line-by-line execution of python

        ResetButton(self.buttons, resetFields=self.fields)
        SubmitButton(self.buttons, self.fields, self._db, resultSection=self.resultSection)           # self.submitButton

