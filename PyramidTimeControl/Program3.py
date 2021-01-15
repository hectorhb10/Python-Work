from tkinter import *
from tkinter import ttk
import time
import datetime

global time_Count 
time_Count = 0

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

        #Clock Output
        self.clock = Label(window, font = ("Owsald 12"))
        self.clock.grid(row = 0, column = 1)
        self.timeScreen()

        #Time Passed Output
        self.time = StringVar()
        self.time.set("00:00:00")
        self.timerLabel = Label(window, textvariable = self.time, font = ("Oswald 12"))
        self.timerLabel.grid(row = 0, column = 2)
        self.startTimer()
      
        #Button Print Screen
        ttk.Button(frame, text = "Print Symbol", command = self.screenOutput ).grid(row = 5, columnspan = 2, sticky = W + E)

        #Button Clean Screen
        ttk.Button(frame, text = "Clean Screen", command = self.stopTimer ).grid(row = 6, columnspan = 2, sticky = W + E)

        #Button Reset Timer
        ttk.Button(frame, text = "Reset Timer", command = self.resetTimer).grid(row = 7, columnspan = 2, sticky = W + E)

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
    
    def timeScreen(self):
        current_time = time.strftime ("%S")
        self.clock["text"] = current_time
        self.clock.after(1000, self.timeScreen)

    def resetTimer(self):
        global time_Count
        time_Count = 1
        self.time.set("00:00:00")
        self.startTimer()
    
    def startTimer(self):
        global time_Count
        time_Count = 0
        self.start_TimerCount()
    
    def start_TimerCount(self):
        global time_Count
        self.timerClock()
    
    def stopTimer(self):
        global time_Count
        time_Count = 1
        self.pyramid.delete("1.0", END)

    def timerClock(self):
        global time_Count
        if(time_Count == 0):
            self.d = str(self.time.get())
            h,m,s = map(int,self.d.split(":"))
            
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            
            self.time.set(self.d)
            if(time_Count==0):
                self.timerLabel.after(930,self.start_TimerCount)



if __name__ == "__main__":
    window = Tk()
    application = Program(window)
    window.mainloop()