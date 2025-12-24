from tkinter.ttk import Spinbox, Frame, Label
from tkinter import StringVar, IntVar
from Assets.MONTHS import months, month_to_number

class DateSelectSection:
    def __init__(self, parent, debug: bool = False):
        self.debug = debug
        self.dateFrame = Frame(parent, padding=(0, 10))
        self.dateFrame.grid()

        # Search Date Label
        Label(self.dateFrame, text="Search Date:").grid(row=0, column=0, padx=5, sticky="w")

        # Date Spinbox
        self.dayVar = IntVar()
        self.dayVar.set(0)
        self.daySpin = Spinbox(self.dateFrame, textvariable=self.dayVar, from_=0, to=31, width=5, wrap=True)
        self.daySpin.grid(row=0, column=1, padx=5)

        # Month Spinbox
        self.monthVar = StringVar()
        self.monthVar.set("Select Month")   # 1rd place where "Select Month is written" and below is second one
        month_values = ("select month",) + tuple(months.values())
        capitalized_months = tuple(word.title() for word in month_values)      # directly the MONTHS file can also be updated
        self.monthSpin = Spinbox(self.dateFrame, 
                                 textvariable=self.monthVar, 
                                 values=capitalized_months, 
                                 width=15, 
                                 wrap=True)
        self.monthSpin.grid(row=0, column=2, padx=5)


    def get(self) -> dict:
        """This function gets the day and month number and returns them in a dictionary"""

        day = self.dayVar.get()
        month_name = self.monthVar.get().lower()

        result = {}

        if day == 0 and month_name == 'select month': raise ValueError("Bro, Don't pass day=0 and month='select month'")

        if day != 0: 
            result["day"] = day

        if month_name != "select month":
            month_number = month_to_number.get(month_name)
            if month_number:
                result["month"] = month_number

        # Debug print
        if (self.debug) and (day == 0) and (month_name == "Select Month"):
            print(f"day: {result.get('day', 'none')}, month: {result.get('month', 'none')}")

        return result

    
    def clear(self):
        self.dayVar.set(0)
        self.monthVar.set("Select Month")   # 3rd place where "Select Month is written"
    
