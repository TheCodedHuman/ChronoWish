# Here we are fabricating the starting point of the ChronoWish app

# Imports
from tkinter import Tk
from tkinter.ttk import Frame
from Components.ChoiceSection import ChoiceSection
from Components.CurDateTimeSection import CurDateTimeSection
from Components.SectionGroup1.SectionGroup1 import SectionGroup1
from Components.SectionGroup2.SectionGroup2 import SectionGroup2
from Components.SectionGroup3.SectionGroup3 import SectionGroup3


# Defined



# Classed
class Base:
    def __init__(self, root):

        # TopLevel Frame
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

        self.group_1 = SectionGroup1(self.dynamicFrame)
        self.group_2 = SectionGroup2(self.dynamicFrame)
        self.group_3 = SectionGroup3(self.dynamicFrame)

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
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    Base(root)
    root.mainloop()
main()

