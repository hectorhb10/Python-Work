from DataLote import *
from tkinter import *
from tkinter import ttk
from threading import Timer
from itertools import islice
import time

count = -1
run = True

data = DataLote()

class Lotes:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Procesamiento por Lotes")
        self.wind.geometry("700x500")
        self.wind ["background"] = "#7D91AF"

        self.minNumberRange = 0
        self.minNumber = -1

        #Process Input
        Label(self.wind, text = "# Process", bg = "#7D91AF").place(x = 30, y = 20)
        self.intiger = IntVar()
        self.process = Entry(self.wind)
        self.process.place(x = 90, y = 20)

        #In Wait Output
        Label(self.wind, text = "On Hold", bg = "#7D91AF").place(x = 60, y = 60)
        Label(self.wind, text = "# Of pending lots:", bg = "#7D91AF").place(x = 40, y = 420)
        self.numberOfLots = StringVar()
        self.numberOfLots.set("0")
        self.numberOfLotsLabel= Label(window, textvariable = self.numberOfLots, bg = "#7D91AF")
        self.numberOfLotsLabel.place(x = 140, y = 420)
        self.wait = Text(window, width = 20, height = 20)
        self.wait.place(x = 10, y = 90)

        #In Execution Output
        Label(self.wind, text = "On Execution", bg = "#7D91AF").place(x = 305, y = 150)
        self.execution = Text(window, width = 20, height = 10)
        self.execution.place(x = 260, y = 180)
        self.time = Label(self.execution, text = "0")

        #Finished
        Label(self.wind, text = "Finished", bg = "#7D91AF").place(x = 555, y = 60)
        self.finished = Text(window, width = 20, height = 20)
        self.finished.place(x = 500, y = 90)

        #Clock Output
        Label(self.wind, text = "Global Clock", bg = "#7D91AF").place(x = 470, y = 20)
        self.timerLabel = Label(window, text = "0", bg = "#7D91AF")
        self.timerLabel.place(x = 545, y = 21)
        self.timerClock()

        #Button Generate Process
        ttk.Button(self.wind, text = "Generate", command = self.mainCall).place(x = 230, y = 17)
        ttk.Button(self.wind, text = "Get results").place(x = 545, y = 430)
    
    def isNumber(self):
        num = self.process.get()
        self.intiger = int(num)
        data.numberOfProcess = self.intiger
        self.minNumberRange = range(-1, data.numberOfProcess)
        self.minNumber = min(self.minNumberRange)
    
    def stopTime(self):
        global run
        run = False

    def startTime(self):
        global run
        run = True
        self.newTime()

    def newTime(self):
        def deletingTime():
            if not run:
                return
            for i in range(data.numberOfProcess):
                data.taskID = i + 1
                if(i == self.minNumber):
                    self.execution.delete('3.5', END)
                    self.execution.insert(INSERT, data.executionTime)
                    self.time.after(1000, deletingTime)
                    data.executionTime -= 1
                if(data.executionTime == -1):
                    self.stopTime()
                    self.execution.delete('1.0', END)
                    self.wait.delete('1.0', END)
                    self.execution.insert(INSERT, data.informationInTable)
                    self.wait.insert(INSERT, data.pendingProcess)
                    self.finished.insert(INSERT, data.finihsProcess)
                    self.startTime()
        deletingTime()
    
    def insertInScreen(self):
        with open("Data-Read.txt") as fin:
            try:
                while True: 
                    datos =  islice(fin, 0, 3)
                    taskID = next(datos)
                    operation = next(datos)
                    timeExecution = next(datos)
                    process = taskID + operation + timeExecution
                    if(int(timeExecution) == 3 ):
                        self.execution.insert(INSERT, "HHHHHH")
                    self.execution.insert(INSERT, process)
                    if():
                        self.wait.insert(INSERT, process)
            except StopIteration:
                pass
    
    def mainCall(self):
        self.isNumber()
        data.insertInFile()
        self.insertInScreen()
        self.startTime()
        self.numberOfLots.set(data.pendingLots)

    def timerClock(self):
        def timerValue():
            global count
            if count == -1:
                show = "0"
            else:
                show = str(count)
            self.timerLabel['text'] = show
            self.timerLabel.after(1000, timerValue)
            count += 1
        timerValue()

if __name__ == "__main__":
    window = Tk()
    application = Lotes(window)
    window.mainloop()