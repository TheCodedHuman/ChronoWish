from tkinter.ttk import Spinbox, Frame, Label
from tkinter import StringVar, IntVar
from Assets.months import months

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
        self.monthVar.set(months[0])            # ['january', ...]
        self.monthSpin = Spinbox(self.dateFrame, textvariable=self.monthVar, values=months, width=10, wrap=True)
        self.monthSpin.grid(row=0, column=2, padx=5)


    def zip_date_month(self) -> int:
        '''This function cleans the date and month value to send forward appropriately'''
        date = self.dayVar.get()                # gets date

        month_val = self.monthVar.get()         # gets name of month
        month = months.index(month_val)         # gets index of month_name

        return date, month


    def get(self):
        day, month = self.zip_date_month()
        return {
            "day": day,
            "month": month
        }
    
    def clear(self):
        self.dayVar.set(1)
        self.monthVar.set(months[0])
    
