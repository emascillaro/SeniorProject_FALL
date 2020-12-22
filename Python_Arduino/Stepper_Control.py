import serial
import pyfirmata
from tkinter import *
from tkinter import ttk

arduinoData = serial.Serial('com3', 9600)

def Forward(enans):
    print(enans)
    arduinoData.write(str.encode('1''enans'))


def Backward():
    arduinoData.write(str.encode('0''10'))

window  = Tk()
window.title("Controlling of the Stepper motor")
en = Entry(window)
en.grid(row =  0, column = 2)
enans = en.get()

try:
    int(enans)
except ValueError:
    pass
btn1 = Button(window, text = "Forward", command = Forward(enans))
btn1.grid(row = 0, column = 0)

btn2 = Button(window, text = "Backward", command = Backward)
btn2.grid(row = 1, column = 0)

window.mainloop()
