# Here we are fabricating the starting point of the ChronoWish app

# Imports
from tkinter import Tk
from tkinter.ttk import Frame
from Components.ChoiceSection import ChoiceSection
from Components.CurDateTimeSection import CurDateTimeSection
from Components.InputSection import InputSection
from Components.DateSelectSection import DateSelectSection
from Components.MainButtons import ResetButton, SubmitButton


# Defined



# Classed
class Base:
    def __init__(self, root):

        # TopLevel Frame
        self.topLevel = Frame(root, padding=15)
        self.topLevel.grid(row=0, column=0, sticky="news")
        self.topLevel.columnconfigure(0, weight=1)

        # Choices Section
        self.choiceInt = ChoiceSection(self.topLevel)

        # Current DateTime Section
        self.dateTime = CurDateTimeSection(self.topLevel)

        # Entry Section
        self.entries = InputSection(self.topLevel)

        # Date Select Section
        self.date = DateSelectSection(self.topLevel)

        # ButtonFrame Section
        self.fields = [self.entries, self.date]                 # each field is providing 2 values currently

        self.buttons = Frame(self.topLevel, padding=(0, 10))
        self.buttons.grid()

        ResetButton(self.buttons, resetFields=self.fields)
        self.submitButton = SubmitButton(self.buttons, submitFields=self.fields)
        


# Literals



# Main
def main():
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    Base(root)
    root.mainloop()
main()

