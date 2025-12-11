from tkinter.ttk import Button


class ResetButton(Button):
    def __init__(self, parent, resetFields: list | tuple):
        super().__init__(parent, text="Reset", command=lambda: self.on_reset(resetFields))
        self.grid(row=0, column=0, padx=10)

    def on_reset(self, fields):
        for section in fields:
            section.clear()
            
        print(f"Resetting fields: {fields}\n")


class SubmitButton(Button):
    def __init__(self, parent, submitFields: list | tuple, db):

        self.db = db
        self.submitFields = submitFields

        super().__init__(parent, text="Search", command=self.on_submit)
        self.grid(row=0, column=1, padx=10)


    def on_submit(self):
        collected = {}

        for section in self.submitFields:
            if hasattr(section, "get"):
                collected.update(section.get())

        result = self.db.fetch_birthday(**collected)

        print(f"Collected data: {collected}")
        print(f"DB result: {result}")
        
        return result

