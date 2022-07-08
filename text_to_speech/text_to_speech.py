from win32com.client import*
from tkinter import*

root = Tk()
a = ""

l1 = Label(text="Enter what you want to here")
l1.pack()

textbox = Entry(relief = "solid",bg = "powderblue",width=30)
textbox.pack()

def speak (text): 
	speak = Dispatch("SAPI.Spvoice")
	speak.Speak(text)

b1 = Button (text="Speak",command = lambda:speak(textbox.get()))
b1.pack()

root.mainloop()