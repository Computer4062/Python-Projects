from tkinter import *
root = Tk()
global num
num = 0
l = Label (root, text = 0)
l.pack()

def Button1Function ():
    global num
    num += 1
    l["text"] = num
    print (num)

def Button2Function ():
    global num
    num-= 1
    l["text"] = num
    print (num)

b1 = Button (root, text = "Click to add",command = Button1Function)
b2 = Button (root, text = "Click to substract",command = Button2Function)
b1.pack()
b2.pack()

root.mainloop()
