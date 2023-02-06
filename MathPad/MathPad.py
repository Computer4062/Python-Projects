from tkinter import *
import pytesseract
import cv2
import pyscreenshot

pytesseract.pytesseract.tesseract_cmd = "D:/Program Files/Tesseract-OCR/tesseract.exe"

window = Tk()

def paint(event):
    color = 'black'
    x1, y1 = (event.x-1),(event.y-1)
    x2, y2 = (event.x+1),(event.y+1)
    Canvas1.create_oval(x1, y1, x2, y2, fill=color, outline=color, width = 10)

def grabImage():
    x1 = 659
    y1 = 230
    x2 = 1282
    y2 = 408
    screenshot = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
    screenshot.save("screenshot.png")

    generate_text("screenshot.png")

def generate_text(image):
    try:
        img = cv2.imread(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (7, 7), 0)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)

        value = pytesseract.image_to_string(img)
        Text1.delete(1.0, END)
        Text1.insert(END, value)
    except:
        insert_text = "Something went wrong check whether you have a file called screenshot.png"
        Text1.delete(0.1, END)
        Text1.insert(END, insert_text)
    finally:
        calculate(value)

def calculate(val):
    try:
        ans = eval(val)
        Text1.delete(1.0, END)
        Text1.insert(END, f"{val} = {ans}")
    except:
        insert_text = f"Something went wrong, what you entered: {val} was probably not an proper equation"
        Text1.delete(1.0, END)
        Text1.insert(END, insert_text)

def readInstructions():
    insert_text = "Write your equation in the math pad clearly without any equal symbol. \n " \
                  "Then press the calculate button to get the answer. \n" \
                  "Remember not to include any unicode characters or move the pad in the process \n" \
                  "Please remember to edit the values in line numbers 17 to 20 before using the application \n"

    Text1.delete(1.0, END)
    Text1.insert(END, insert_text)

def ClearButton(): Canvas1.delete("all")


window.geometry("606x512+660+210")
window.minsize(120, 1)
window.maxsize(1924, 1061)
window.resizable(False, False)
window.title("windowlevel 0")
window.configure(background="#d9d9d9")

window = window

Canvas1 = Canvas(window)
Canvas1.configure(background="#ffffff")
Canvas1.configure(borderwidth="2")
Canvas1.configure(cursor="fleur")
Canvas1.configure(insertbackground="black")
Canvas1.configure(relief="ridge")
Canvas1.configure(selectbackground="#ffffff")
Canvas1.configure(selectforeground="black")
Canvas1.place(relx=0.0, rely=0.0, relheight=0.496, relwidth=1.005)
Canvas1.bind('<B1-Motion>', paint)
Clearbtn = Button(window)
Clearbtn.place(relx=0.017, rely=0.506, height=44, width=267)
Clearbtn.configure(activebackground="beige")
Clearbtn.configure(activeforeground="black")
Clearbtn.configure(background="#d9d9d9")
Clearbtn.configure(compound='left')
Clearbtn.configure(disabledforeground="#a3a3a3")
Clearbtn.configure(foreground="#000000")
Clearbtn.configure(highlightbackground="#d9d9d9")
Clearbtn.configure(highlightcolor="black")
Clearbtn.configure(pady="0")
Clearbtn.configure(text='''Clear''')
Clearbtn.configure(command=ClearButton)
Instructionsbtn = Button(window)
Instructionsbtn.place(relx=0.5, rely=0.506, height=44, width=287)
Instructionsbtn.configure(activebackground="beige")
Instructionsbtn.configure(activeforeground="black")
Instructionsbtn.configure(background="#d9d9d9")
Instructionsbtn.configure(compound='left')
Instructionsbtn.configure(disabledforeground="#a3a3a3")
Instructionsbtn.configure(foreground="#000000")
Instructionsbtn.configure(highlightbackground="#d9d9d9")
Instructionsbtn.configure(highlightcolor="black")
Instructionsbtn.configure(pady="0")
Instructionsbtn.configure(text='''Read Instructions''')
Instructionsbtn.configure(command=readInstructions)
Text1 = Text(window)
Text1.place(relx=0.033, rely=0.738, relheight=0.209, relwidth=0.941)
Text1.configure(background="white")
Text1.configure(font="TkTextFont")
Text1.configure(foreground="black")
Text1.configure(highlightbackground="#d9d9d9")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="black")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(wrap="word")
Calculatebtn = Button(window)
Calculatebtn.place(relx=0.017, rely=0.623, height=44, width=577)
Calculatebtn.configure(activebackground="beige")
Calculatebtn.configure(activeforeground="black")
Calculatebtn.configure(background="#d9d9d9")
Calculatebtn.configure(compound='left')
Calculatebtn.configure(disabledforeground="#a3a3a3")
Calculatebtn.configure(foreground="#000000")
Calculatebtn.configure(highlightbackground="#d9d9d9")
Calculatebtn.configure(highlightcolor="black")
Calculatebtn.configure(pady="0")
Calculatebtn.configure(text='''Calculate''')
Calculatebtn.configure(command=grabImage)

if __name__ == "__main__":
    window.mainloop()