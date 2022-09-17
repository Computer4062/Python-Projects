from win32com.client import*

def speak(text):
    speech = dispatch('SAPI.Spvoice')
    speech.Speak(text)
    exit()
    
speak("new person detected")


