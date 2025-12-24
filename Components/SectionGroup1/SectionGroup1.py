from tkinter.ttk import Frame
from .InputSection import InputSection
from .DateSelectSection import DateSelectSection
from .MainButtons import ResetButton, SubmitButton
from .ResultSection import ResultSection
from Utils.validate_util import validate_values

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
        self.date = DateSelectSection(self.groupFrame, debug=True)

        # ButtonFrame Section
        self.fields = [self.entries, self.date]                 # each field is providing 2 values currently

        self.buttons = Frame(self.groupFrame, padding=(0, 10))
        self.buttons.grid()

        # Intel Table and ProgressBar Section
        self.resultSection = ResultSection(self.groupFrame)     # had to call earlier due to line-by-line execution of python

        ResetButton(self.buttons, resetFields=self.fields)
        self.submitButton = SubmitButton(self.buttons, self.fields, self._db, self.resultSection, debug=True)

        # Bind validation to field changes
        self.date.dayVar.trace_add("write", self.is_form_valid)
        self.date.monthVar.trace_add("write", self.is_form_valid)

        # Initial validation
        self.is_form_valid()


    def is_form_valid(self, *args) -> None:         # args nullify extra stuff like events or more
        """
        Checks date fields
        Disable submitButton: if day=0 and month='select month'
        Enables it otherwise
        """
        
        unsafe_pairs = {
            "day": 0,
            "month": "select month"}

        if validate_values(self.date.get(), check=unsafe_pairs):
            print("validated")
            self.submitButton.state(['!disabled'])
        else:
            self.submitButton.state(["disabled"])

