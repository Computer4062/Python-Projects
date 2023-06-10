import pyautogui
import time
import threading
import tkinter as tk

win = tk.Tk()
win.geometry('500x500')
win.title('Auto Writer')
win.resizable(False, False)

class AutoWriter:
    def __init__(self):
        self.on = False
        self.text = ''
        self.interval = 0.05

    def StartWriting(self):
        time.sleep(5)

        self.on = True
        if self.on:
            pyautogui.typewrite(self.text, interval = self.interval)

    def StopWriting(self):
        self.on = False

autoWriter = AutoWriter()

StartWriting = threading.Thread(target = autoWriter.StartWriting)
StopWriting = threading.Thread(target = autoWriter.StopWriting)

def Start(function = StartWriting):
    autoWriter.text = text.get(1.0, tk.END)
    autoWriter.interval = interval.get()
    function.start()
    label.configure(text = 'typing')

def Stop(function = StopWriting):
    function.start()
    label.configure(text = ' ')

text = tk.Text(win)
interval = tk.Entry(win, width = 200)
start = tk.Button(win, text = 'start', command = Start, width = 200)
stop = tk.Button(win, text = 'stop', command = Stop, width = 200)
label = tk.Label(win, text = '')

text.pack()
interval.pack()
start.pack()
stop.pack()
label.pack()

if __name__ == '__main__':
    win.mainloop()