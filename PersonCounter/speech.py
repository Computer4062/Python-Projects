import cv2
from win32com.client import*

def speak(text):
    speech = dispatch('SAPI.Spvoice')
    speech.Speak(text)
    exit()
    
speak("new person detected")

cv2.waitKey(0)


