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
    def __init__(self, parent, submitFields: list | tuple):
        super().__init__(parent, text="Search", command=lambda: self.on_submit(submitFields))
        self.grid(row=0, column=1, padx=10)

    def on_submit(self, fields):
        collected = {}

        for section in fields:
            if hasattr(section, "get"):
                collected.update(section.get())

        print(collected)

