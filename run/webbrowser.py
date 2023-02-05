import webbrowser
from tkinter import*
from PIL import*
from PIL import ImageTk, Image

win = Tk()
win.iconbitmap("icon2.ico")
win.configure(bg='white')
win.title("run")

def buttonFunction():
    url = textbox.get()
    webbrowser.open(url)

img = ImageTk.PhotoImage(Image.open("icon2.png"))

l4 = Label(text="Enter a url or a application name to open \n and this programme would open it up for you")
l4.configure(bg="white")
l4.grid(row=0,column=2)

l3 = Label(text="Open:")
l3.configure(bg="white")
l3.grid(row=1,column=0)

l2 = Label(image = img,width=50,height=50)
l2.configure(bg='white')
l2.grid(row=0,column=0)

textbox = Entry(width=50)
textbox.grid(row=1,column=2)
btn1 = Button(text="Enter",command=buttonFunction)
btn1.grid(row=1,column=3)

if __name__ == "__main__":
    win.mainloop()
