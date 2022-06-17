from tkinter import *
import random
import time
from threading import Thread

root = Tk()
score = 0
root.geometry("500x500")
global x_place
x_place = 0
global y_place
y_place = 0
global clicks
clicks = 0
global time_sec
time_sec = 10

l1 = Label (root, text = clicks)
l2 = Label (root, text = clicks)
l1.pack()
l2.pack()

def click_count ():
    global clicks
    x_place = random.randint (0,500)
    y_place = random.randint (0,500)
    t_f = random.randint (1,2)
    b1.place (x = x_place , y = y_place)
    clicks += 1
    l1["text"] = "clicks:",clicks

def timer ():
    global time_sec
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        l2 ["text"] = time_sec
        
def ButtonFunction ():
    if __name__ == "__main__":
        Thread (target = click_count).start()
        Thread (target = timer).start()
        
b1 = Button (root, text = "click here to score",command = ButtonFunction)
b1.pack()


root.mainloop()