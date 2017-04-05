"""Gavin Franklin
   4/6/2016
   BMI Calculator"""

#This code imports the tkinter library to build the gui
from tkinter import *

#This code creates the class under Tkinter to make the gui
class App (Tk):
    def __init__(self):
        Tk.__init__(self)
        

        #this code creates the top of the gui
        self.weilbl = Label(self, text = "Weight:")
        self.weilbl.grid(row = 0, column = 0)

        self.Heilbl = Label(self, text = "Height:")
        self.Heilbl.grid(row = 1, columnspan = 2)

        self.feelbl = Label(self, text = "Feet:")
        self.feelbl.grid(row = 2, column = 0)

        self.inclbl = Label(self, text = "Inches:")
        self.inclbl.grid(row = 3, column = 0)

        self.weiinp = Entry(self)
        self.weiinp.grid(row = 0, column = 1)

        self.feeinp = Entry(self)
        self.feeinp.grid(row = 2, column = 1)

        self.incinp = Entry(self)
        self.incinp.grid(row = 3, column = 1)

        #this code creates the bottom half of the program

        self.button = Button(self, text = "Calculate", command = self.calc)
        self.button.grid(row = 4, columnspan = 2)

        self.bmilbl = Label(self, text = "BMI:")
        self.bmilbl.grid(row = 5, column = 0)

        self.catlbl = Label(self, text = "Catagory:")
        self.catlbl.grid(row = 6, column = 0)

        #This code creates Labels that appear as text boxes
        self.numlbl = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        self.numlbl.grid(row = 5, column = 1)

        self.worlbl = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        self.worlbl.grid(row = 6, column = 1)

    def calc(self):
        self.inches = ((float(self.feeinp.get()))*12) + (float(self.incinp.get()))
        self.weight = float(self.weiinp.get())
        self.bmi = (self.weight / (self.inches **2)) * 703
        self.bmi = round(self.bmi, 2)
        self.numlbl["text"] = self.bmi
        if self.bmi > 18.5:
            if self.bmi > 24.9:
                if self.bmi > 25:
                    if self.bmi > 30:
                        self.worlbl["text"] = "obese"
                else:
                    self.worlbl["text"] = "overweight"
            else:
                self.worlbl["text"] = "normal weight"
        else:
            self.worlbl["text"] = "underweight"

#This code creates the main loop
def main():
    a = App()
    a.mainloop()
#This code runs the main loop if the program is ran on the comman line
if __name__ == "__main__":
    main()
