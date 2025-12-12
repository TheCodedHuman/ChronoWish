# Here we are fabricating the starting point of the ChronoWish app

# Imports
from pathlib import Path
from tkinter import Tk
from tkinter.ttk import Frame
from Components.ChoiceSection import ChoiceSection
from Components.CurDateTimeSection import CurDateTimeSection
from Components.SectionGroup1.SectionGroup1 import SectionGroup1
from Components.SectionGroup2.SectionGroup2 import SectionGroup2
from Components.SectionGroup3.SectionGroup3 import SectionGroup3
from Database.db import ChronoDB


# Classed
class Base:
    def __init__(self, root, db):

        # TopLevel Frame
        self.db = db
        self.topLevel = Frame(root, padding=15)
        self.topLevel.grid(row=0, column=0, sticky="news")
        self.topLevel.columnconfigure(0, weight=1)

        #-------------------------------------------------------#

        # Choices Section
        self.choiceInt = ChoiceSection(self.topLevel)
        self.choiceInt.set_callback(self.switch_section)

        # Current DateTime Section
        self.dateTime = CurDateTimeSection(self.topLevel)

        #-------------------------------------------------------#

        # Sub-Frame containing groups
        self.dynamicFrame = Frame(self.topLevel)
        self.dynamicFrame.grid(sticky="news")
        self.dynamicFrame.columnconfigure(0, weight=1)

        self.group_1 = SectionGroup1(self.dynamicFrame, self.db)
        self.group_2 = SectionGroup2(self.dynamicFrame, self.db)
        self.group_3 = SectionGroup3(self.dynamicFrame, self.db)

        # Hide all groups initially and call the switch_section manually
        self.group_1.groupFrame.grid_remove()
        self.group_2.groupFrame.grid_remove()
        self.group_3.groupFrame.grid_remove()
        self.switch_section(self.choiceInt.choiceVar.get())


    def switch_section(self, choice: int):

        # Initially hiding all groups
        self.group_1.groupFrame.grid_remove()
        self.group_2.groupFrame.grid_remove()
        self.group_3.groupFrame.grid_remove()

        # Manipulation
        match choice:
            case 1: self.group_1.groupFrame.grid()
            case 2: self.group_2.groupFrame.grid()
            case 3: self.group_3.groupFrame.grid()


# Main
def main():

    # Base Window
    root = Tk()
    root.title("ChronoWish")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Database initiation
    db_path = Path(__file__).parent / "Database" / "chronowish.db"
    db = ChronoDB(db_path)

    # Base App
    Base(root, db)
    root.mainloop()

main()

