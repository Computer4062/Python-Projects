import datetime
from tkinter import*

win = Tk()

def getTime():
    time = datetime.datetime.now()
    l1.configure(text=time)
    
l1 = Label(text = "0")
btn1 = Button(text="get time", command=getTime)

l1.pack()
btn1.pack()

if __name__ == "__main__":
    win.mainloop()