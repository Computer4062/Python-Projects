import os
import pyautogui
from tkinter import *

root = Tk()

l1 = Label (root, text = "select any of these options")
l1.pack()

def Button1Function ():
    pyautogui.alert ("Your computer will shutdown")
    os.system ("shutdown /s /t 1")

def Button2Function ():
    pyautogui.alert ("your computer will restart")
    os.system ("shutdown /r /t 1")

b1 = Button (root, text = "click here to shutdoown",command = Button1Function)
b2 = Button (root, text = "click here to restart",command = Button2Function)
b1.pack(side = "left")
b2.pack(side = "right")

root.mainloop()
