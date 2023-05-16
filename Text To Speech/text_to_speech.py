from win32com.client import Dispatch
from tkinter import Entry, Tk, Button

def speak(text):
    speak = Dispatch("SAPI.SpVoice")
    voices = speak.GetVoices()
    for voice in voices:
        if "Microsoft Zira Desktop" in voice.GetDescription():
            speak.Voice = voice
            break
    speak.Speak(text)

root = Tk()
root.title("Speaker")

textbox = Entry(relief = "solid", width=30)
textbox.grid(row = 0, column = 0)

b1 = Button (text="Speak",command = lambda:speak(textbox.get()), justify = 'center')
b1.grid(row = 0, column = 1)

root.mainloop()
