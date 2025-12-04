from tkinter import IntVar
from tkinter.ttk import Frame, Radiobutton

class ChoiceSection:
        def __init__(self, parent: Frame):

            # Frame containing options
            self.choiceFrame = Frame(parent, padding=(0, 10))        
            self.choiceFrame.grid()
            
            self.choiceVar = IntVar()           # value=1 can also be used
            self.choiceVar.set(1)

            # RadioButtons within it
            self.findBirth = Radiobutton(self.choiceFrame, text="Find Birthday By Date", variable=self.choiceVar, value=1)
            self.findBirth.grid(row=0, column=0, sticky="we", padx=10)

            self.findNear = Radiobutton(self.choiceFrame, text="Find Nearest Birthday", variable=self.choiceVar, value=2)
            self.findNear.grid(row=0, column=1, sticky="we", padx=10)

            self.uploadBirth = Radiobutton(self.choiceFrame, text="Upload Birthday", variable=self.choiceVar, value=3)
            self.uploadBirth.grid(row=0, column=2, sticky="we", padx=10)


        def getChoice(self):
            return self.choiceVar.get()
        

        # DeBug
        def onChoiceChange(self, *args):
            print("Selected:", self.getChoice())

