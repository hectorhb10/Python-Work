from tkinter import *
from tkinter import ttk

class Program:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Program 3")
        self.wind.geometry("900x500")
        self.wind ["background"] = "#7D91AF"

        #Creating Frame Container
        frame = LabelFrame(self.wind, text = "Programming Diagnosis")
        frame.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        #Symbol Input
        Label(frame, text = "Add the Symbol", font = ("Oswald 12")).grid(row = 1, column = 0)
        self.symbol = Entry(frame)
        self.symbol.focus()
        self.symbol.grid(row = 1, column = 1)

        #Number Input
        Label(frame, text = "Add the Number", font = ("Oswald 12")).grid(row = 2, column = 0)
        self.number = Entry(frame)
        self.number.grid(row = 2, column = 1)

        #Pyramid Output
        self.pyramid = Text(window, width = 50, height = 20)
        self.pyramid.grid(row = 1, column = 1, padx = 5, pady = 5)

      
        #Button Print Screen
        ttk.Button(frame, text = "Print Symbol", command = self.screenOutput ).grid(row = 5, columnspan = 2, sticky = W + E)

        #Button Clean Screen
        ttk.Button(frame, text = "Clean Screen", command = self.pyramid.delete("1.0", END) ).grid(row = 6, columnspan = 2, sticky = W + E)

    def screenOutput(self):
        symbolList = ['!', '@', '#', '$', '%', '&', '*', '=', '+', '-']
        symbolVar = ""
        symbolVar = self.symbol.get()
        if symbolVar in symbolList:
            if self.number.get().isnumeric() == True:
                self.pyramidCreation()
            else:
                self.pyramid.delete('1.0', END)
                self.pyramid.insert(INSERT, "Error Not a Number")
        else:
            self.pyramid.delete('1.0', END)
            self.pyramid.insert(INSERT, "Error Not a Symbol")
    
    def pyramidCreation(self):
        global pyramid_created
        sizePyramid = self.number.get()
        symbolUsed = self.symbol.get()
        for i in range(int(sizePyramid)):
            pyramidOperation = (' ' * (int(sizePyramid) - i - 1) + symbolUsed * (2 * i + 1 ))
            self.pyramid.insert(INSERT, pyramidOperation)
            self.pyramid.insert(END, '\n')
            print(pyramidOperation)
            pyramid_created = True

if __name__ == "__main__":
    window = Tk()
    application = Program(window)
    window.mainloop()