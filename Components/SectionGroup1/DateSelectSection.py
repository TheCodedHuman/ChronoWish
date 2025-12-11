from tkinter.ttk import Spinbox, Frame, Label
from tkinter import StringVar, IntVar
from Assets.months import months, month_to_number

class DateSelectSection:
    def __init__(self, parent):
        self.dateFrame = Frame(parent, padding=(0, 10))
        self.dateFrame.grid()

        # Search Date Label
        Label(self.dateFrame, text="Search Date:").grid(row=0, column=0, padx=5, sticky="w")

        # Date Spinbox
        self.dayVar = IntVar()
        self.dayVar.set(1)
        self.daySpin = Spinbox(self.dateFrame, textvariable=self.dayVar, from_=1, to=31, width=5, wrap=True)
        self.daySpin.grid(row=0, column=1, padx=5)

        # Month Spinbox
        self.monthVar = StringVar()
        self.monthVar.set(months.get(1))            # 'january'
        self.monthSpin = Spinbox(self.dateFrame, 
                                 textvariable=self.monthVar, 
                                 values=tuple(months.values()), 
                                 width=10, 
                                 wrap=True)
        self.monthSpin.grid(row=0, column=2, padx=5)


    def get(self) -> dict:
        """This function gets the day and month number and returns them in a dictionary"""

        day = self.dayVar.get()
        month_name = self.monthVar.get()
        month_number = month_to_number[month_name]

        return {
            "day": day,
            "month": month_number
        }
    
    def clear(self):
        self.dayVar.set(1)
        self.monthVar.set(months[1])
    
