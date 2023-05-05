from win32com.client import Dispatch
from tkinter import Entry, Tk, Button

root = Tk()
root.title("Speaker")

textbox = Entry(relief = "solid", width=30)
textbox.grid(row = 0,column = 0)

def speak (text):
	speak = Dispatch("SAPI.Spvoice")
	speak.Speak(text)

b1 = Button (text="Speak",command = lambda:speak(textbox.get()))
b1.grid(row = 0,column = 1)

root.mainloop()
