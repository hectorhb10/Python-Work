from tkinter import ttk
from tkinter import *

class Program:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Program 1")

        #Creating Frame Container
        frame = LabelFrame(self.wind, text = "Programming Diagnosis")
        frame.grid(row = 0, column = 0, padx = 0, pady = 5)

        #Symbol Input
        Label(frame, text = "Add the Symbol", font = ("Oswald 12")).grid(row = 1, column = 0)
        self.symbol = Entry(frame)
        self.symbol.focus()
        self.symbol.grid(row = 1, column = 1)

        #Number Input
        Label(frame, text = "Add the Number", font = ("Oswald 12")).grid(row = 2, column = 0)
        self.number = Entry(frame)
        self.number.grid(row = 2, column = 1)

        #Screen Output
        Label(frame, text = "Return the Value", font = ("Oswald 12")).grid(row = 4, column = 0)
        self.screenReturn = Entry(frame)
        self.screenReturn.grid(row = 4, column = 1)

        #Button Print Screen
        ttk.Button(frame, text = "Print Symbol", command = self.screenOutput ).grid(row = 5, columnspan = 2, sticky = W + E)

    def screenOutput(self):
        symbolList = ['!', '@', '#', '$', '%', '&', '*', '=', '+', '-']
        symbolVar = ""
        symbolVar = self.symbol.get()
        if symbolVar in symbolList:
            if self.number.get().isnumeric() == True:
                self.screenReturn.delete(0, END)
                self.screenReturn.insert(0, self.symbol.get())
            else:
                self.screenReturn.delete(0, END)
                self.screenReturn.insert(0, "Error Not a Number")
        else:
            self.screenReturn.delete(0, END)
            self.screenReturn.insert(0, "Error Not a Symbol")
        

if __name__ == "__main__":
    window = Tk()
    application = Program(window)
    window.mainloop()