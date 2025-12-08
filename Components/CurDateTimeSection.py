import datetime
from  tkinter.ttk import Frame, Label

class CurDateTimeSection:
    def __init__(self, parent: Frame):
        self.timeFrame = Frame(parent, padding=(0, 10), relief="solid")
        self.timeFrame.grid()
        self.timeFrame.columnconfigure(0, weight=1)
        self.timeFrame.columnconfigure(1, weight=1)

        # Date Label
        self.dateLabel = Label(self.timeFrame, text="")
        self.dateLabel.grid(row=0, column=0, sticky="we", padx=40)

        # Time Label
        self.timeLabel = Label(self.timeFrame, text="")
        self.timeLabel.grid(row=0, column=1, sticky="we", padx=40)

        # Update time per second
        self.update_datetime()


    # Periodic time updater
    def update_datetime(self):

        now = datetime.datetime.now()
        dateStr = now.strftime("%d %B %Y")                          # this can be optimized
        timeStr = now.strftime("%I:%M:%S %p")

        self.dateLabel.config(text=f"Today's Date:\n{dateStr}")
        self.timeLabel.config(text=f"Current Time:\n{timeStr}")

        self.timeFrame.after(1000, self.update_datetime)            # Event Loop

