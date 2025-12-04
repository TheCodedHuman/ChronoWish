# Here we are fabricating the starting point of the ChronoWish app

# Imports
from tkinter import Tk
from tkinter.ttk import Frame
from Components.ChoiceSection import ChoiceSection
from Components.CurDateTimeSection import CurDateTimeSection
from Components.InputSection import InputSection


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


# Literals



# Main
def main():
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    Base(root)
    root.mainloop()
main()

