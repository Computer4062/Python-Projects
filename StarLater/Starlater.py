from googletrans import Translator, LANGUAGES
import tkinter as tk

win = tk.Tk()
win.title('translator')
win.geometry('500x500')
win.resizable()

def FindLanguage(dictionary, value):
    language = ''
    for key, val in dictionary.items():
        if val == value:
            language = key

    return language

def Translate():
    translatedText.delete('1.0', tk.END)

    translator = Translator(service_urls = ['translate.google.com'])

    try:
        targetLanguage = FindLanguage(LANGUAGES, language.get().lower())
        result = translator.translate(text.get('1.0', tk.END).lower(), dest = targetLanguage)
        translatedText.insert(tk.END, result.text)

    except:
        translatedText.insert(tk.END, 'Something went wrong')

#main title
    
label = tk.Label(win, text = 'StarLater', font=('Arial', 32))
label.pack()

#frame elements

#initialize frame
frame = tk.Frame(win)
frame.pack()

label = tk.Label(frame, text = 'Language: ', font=('Arial', 16))
label.grid(row = 0, column = 0)

#language textbox
language = tk.Entry(frame)
language.grid(row = 0, column = 1)

#window elements

#text to translate
text = tk.Text(win, width = 150, height = 10)
text.pack()

#translate button
button = tk.Button(win, text = 'Translate', width = 150, command = Translate)
button.pack()

#translated text
translatedText = tk.Text(win, width = 150, height = 10)
translatedText.pack()

if __name__ == '__main__':
    win.mainloop()