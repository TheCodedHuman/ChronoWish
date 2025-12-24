from tkinter.ttk import Button
from Utils.validate_util import validate_values


class ResetButton(Button):
    def __init__(self, parent, resetFields: list | tuple):
        super().__init__(parent, text="Reset", command=lambda: self.on_reset(resetFields))
        self.grid(row=0, column=0, padx=10)

    def on_reset(self, fields):
        for section in fields:
            section.clear()
            
        print(f"Resetting fields: {fields}\n")


class SubmitButton(Button):
    def __init__(self, parent, submitFields: list | tuple, db, resultSection, debug: bool = False):

        self._db = db
        self.debug = debug
        self.submitFields = submitFields
        self.resultSection = resultSection

        super().__init__(parent, text="Search", command=self.on_submit)
        self.grid(row=0, column=1, padx=10)
        self.state(['disabled'])            # initiate it being disabled


    def on_submit(self) -> list[tuple[int | str]]:
        """Task of on_submit is to get data from the db and store in result"""

        collected = {}

        for section in self.submitFields:
            if hasattr(section, "get"):
                collected.update(section.get())

        result: list[tuple] = self._db.fetch_birthday(**collected)              # this is where first time tkinter getting data

        self.resultSection.update_results(result) 
        # this is redirecting towards resultSection and col_order is also there, so better if resultSection itself handles it
        # also, its submit "button" so better it does the work of button rather than processing

        if self.debug:
            print(f"Collected data: {collected}")
            print(f"DB result: {result}\n")
        
        return result

