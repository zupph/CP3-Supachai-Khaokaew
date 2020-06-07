from tkinter import *
import math
def leftClickButtond(event):
    resultBMI = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get())/100,2)
    if resultBMI > 30:
        labelResult.configure(text= "อ้วนมาก")
    elif resultBMI >= 25 and resultBMI < 29.9:
        labelResult.configure(text="อ้วน")
    elif resultBMI >= 23 and resultBMI < 24.9:
        labelResult.configure(text="น้ำหนักเกิน")
    elif resultBMI >= 18.6 and resultBMI < 22.9:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeight = Label(MainWindow, text= "Height (cm)")
labelHeight.grid(row=0, column=0)
labelWeight = Label(MainWindow, text= "Weight (Kg)")
labelWeight.grid(row=1, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
button = Button(MainWindow, text=" Click me")
button.grid(row=2, column=0)
button.bind("<Button-1>", leftClickButtond)
labelResult = Label(MainWindow, text= "ผลลัพธ์")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()