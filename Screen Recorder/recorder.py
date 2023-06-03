import tkinter as tk
import cv2
import numpy as np
import pyautogui
import threading

class Record:
    def __init__(self):
        self.resolution = (1920, 1080)
        self.codec = cv2.VideoWriter_fourcc(*"XVID")

        self.filename = 'Recording.avi'
        self.fps = 10

        self.on = False

    def StartRecording(self):
        try:
            out = cv2.VideoWriter(self.filename, self.codec, self.fps, self.resolution)

            self.on = True
            while self.on == True:
                img = pyautogui.screenshot()

                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                out.write(frame)

            cv2.destroyAllWindows()
            out.release()

        except Exception as error:
            print(error)

    def StopRecording(self):
        self.on = False

record = Record()

StarRecording = threading.Thread(target = record.StartRecording)
StopRecording = threading.Thread(target = record.StopRecording)

def start(function = StarRecording):
    try:
        Label.configure(text = 'Recording')
        record.fps = int(fpsBox.get())
        function.start()
    except Exception as error:
        print(error)

def stop(function = StopRecording):
    Label.configure(text = 'Saved')
    function.start()

#window elements

win = tk.Tk()
win.title('Recorder')
win.geometry('200x270')
win.resizable(False, False)

startButton = tk.Button(win, text = 'StartRecording', width = 50, height = 10, command = start)
startButton.pack()

stopButton = tk.Button(win, text = 'stopRecording', width = 200, command = stop)
stopButton.pack()

#leave a gap

gap = tk.Label(win)
gap.pack()

#frame elements

frame = tk.Frame()
frame.pack()

fpsLabel = tk.Label(frame, text = 'fps: ')
fpsLabel.grid(row = 0, column = 0)

fpsBox = tk.Entry(frame)
fpsBox.grid(row = 0, column = 1)

#status label

gap2 = tk.Label(win)
gap2.pack()

Label = tk.Label(win)
Label.pack()


if __name__ == '__main__':
    win.mainloop()