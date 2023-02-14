from tkinter import *
import time
from threading import Thread

global clicks
clicks = 0
global time_sec
time_sec = 10
global cps
cps = 0
        
def click_count ():
    global cps
    global clicks
    clicks += 1
    Clicks_l["text"] = clicks

def timer ():
    global clicks 
    global time_sec
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_sec -= 1
        Time_l ["text"] = time_sec
        
        if Time_l["text"] == 0:
            print (clicks)
            cps = clicks / 10
            cps_l["text"] = "cps:",cps
            
def Button1Function ():
    Thread (target = click_count).start()
    
def Button2Function ():
    global clicks
    clicks = 0
    global cps
    cps = 0
    global time_sec
    time_sec = 10
    Thread (target = timer).start()

window = Tk()

window.geometry("600x450+660+210")
window.minsize(120, 1)
window.maxsize(1924, 1061)
window.resizable(1,  1)
window.title("windowlevel 0")
window.configure(background="#d9d9d9")
    
window = window
   
Clicks_l = Label(window)
Clicks_l.place(relx=0.05, rely=0.067, height=21, width=34)
Clicks_l.configure(anchor='w')
Clicks_l.configure(background="#d9d9d9")
Clicks_l.configure(compound='left')
Clicks_l.configure(disabledforeground="#a3a3a3")
Clicks_l.configure(foreground="#000000")
Clicks_l.configure(text='''0''')
Label2 = Label(window)
Label2.place(relx=0.133, rely=0.067, height=21, width=34)
Label2.configure(anchor='w')
Label2.configure(background="#d9d9d9")
Label2.configure(compound='left')
Label2.configure(cursor="fleur")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(foreground="#000000")
Label2.configure(text='''clicks''')
Button1 = Button(window)
Button1.place(relx=0.05, rely=0.178, height=194, width=547)
Button1.configure(activebackground="beige")
Button1.configure(activeforeground="black")
Button1.configure(background="#d9d9d9")
Button1.configure(compound='left')
Button1.configure(cursor="fleur")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Click here to get started''')
Button1.configure(command = Button1Function)
Time_l = Label(window)
Time_l.place(relx=0.383, rely=0.067, height=21, width=34)
Time_l.configure(anchor='w')
Time_l.configure(background="#d9d9d9")
Time_l.configure(compound='left')
Time_l.configure(disabledforeground="#a3a3a3")
Time_l.configure(foreground="#000000")
Time_l.configure(text='''0''')
Label4 = Label(window)
Label4.place(relx=0.5, rely=0.067, height=21, width=34)
Label4.configure(anchor='w')
Label4.configure(background="#d9d9d9")
Label4.configure(compound='left')
Label4.configure(disabledforeground="#a3a3a3")
Label4.configure(foreground="#000000")
Label4.configure(text='''time''')
cps_l = Label(window)
cps_l.place(relx=0.75, rely=0.067, height=21, width=34)
cps_l.configure(anchor='w')
cps_l.configure(background="#d9d9d9")
cps_l.configure(compound='left')
cps_l.configure(disabledforeground="#a3a3a3")
cps_l.configure(foreground="#000000")
cps_l.configure(text='''0''')
Label6 = Label(window)
Label6.place(relx=0.833, rely=0.067, height=21, width=34)
Label6.configure(anchor='w')
Label6.configure(background="#d9d9d9")
Label6.configure(compound='left')
Label6.configure(disabledforeground="#a3a3a3")
Label6.configure(foreground="#000000")
Label6.configure(text='''cps''')
Button2 = Button(window)
Button2.place(relx=0.05, rely=0.644, height=54, width=547)
Button2.configure(activebackground="beige")
Button2.configure(activeforeground="black")
Button2.configure(background="#d9d9d9")
Button2.configure(compound='left')
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''Click here to start the timer''')
Button2.configure(command = Button2Function)


if __name__ == "__main__":
    window.mainloop()
