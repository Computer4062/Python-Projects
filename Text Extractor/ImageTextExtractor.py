from tkinter import *
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "D:/Program Files/Tesseract-OCR/tesseract.exe"

window = Tk()

global text

def GetText(image_path):
    try:
        img_recorded = cv2.imread(image_path)
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (7,7), 0)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                  cv2.THRESH_BINARY, 11, 2)

        value = pytesseract.image_to_string(img)

        Text1.delete(1.0, END)
        Text1.insert("end-1c", value)

        hImg, wImg = img.shape
        boxes = pytesseract.image_to_boxes(img)

        for b in boxes.splitlines():
            b = b.split(' ')
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img_recorded, (x, hImg - y), (w, hImg - h), (0, 255, 0), 2)

        cv2.imshow("image", img_recorded)
        cv2.waitKey(0)

    except:
        Text1.delete(1.0, END)
        Text1.insert("end-1c", "The file was not found or the file type is not surpported")

def getTextLive():
    # define a video capture object
    try:
        vid = cv2.VideoCapture(0)
        while (True):
            ret, frame = vid.read()
            show = frame
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img = cv2.GaussianBlur(img, (7, 7), 0)
            img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                        cv2.THRESH_BINARY, 11, 2)
            hImg, wImg = img.shape
            boxes = pytesseract.image_to_boxes(img)

            for b in boxes.splitlines():
                b = b.split(' ')
                x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
                cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,255,0), 2)

            value = pytesseract.image_to_string(img)

            global text
            text = value

            if cv2.waitKey(1) == ord('h'): show = img

            cv2.imshow('frame', show)
            cv2.waitKey(1)

        vid.release()
        cv2.destroyAllWindows()

        Text1.delete(1.0, END)
        Text1.insert(END, text)

    except:
        Text1.delete(1.0, END)
        Text1.insert(END, "Something went wrong with opencv-python check whether your camera is connected properly, if not it is a problem with your installed package of opencv")

def readInstructions():
    value = "Enter the location of the image which holds the text you want to extract \n" \
            "Then a pop up would appear with the text in your text file extracted \n" \
            "You can copy this text through the text box \n" \
            "The image would be thresh holded, blured and converted to gray so that it is easier to detect \n" \
            "\n" \
            "For live text extraction show the image to the camera \n" \
            "And once the camera detects the text you can close the application and copy the text \n" \
            "Press h to show the in extracting view \n"

    Text1.delete(1.0, END)
    Text1.insert("end-1c", value)

window.geometry("600x450+660+210")
window.minsize(120, 1)
window.maxsize(1924, 1061)
window.resizable(False, False)
window.title("windowlevel 0")
window.configure(background="#d9d9d9")
window = window
Button1 = Button(window)
Button1.place(relx=0.033, rely=0.733, height=44, width=257)
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
Button1.configure(text="Extract Text Live")
Button1.configure(command = getTextLive)
Label1 = Label(window)
Label1.place(relx=0.383, rely=0.022, height=40, width=254)
Label1.configure(anchor='w')
Label1.configure(background="#d9d9d9")
Label1.configure(compound='left')
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#000000")
Label1.configure(text="TEXT EXTRACTER")
Entry1 = Entry(window)
Entry1.place(relx=0.467, rely=0.156, height=30, relwidth=0.473)
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")
Button2 = Button(window)
Button2.place(relx=0.05, rely=0.156, height=34, width=237)
Button2.configure(activebackground="beige")
Button2.configure(activeforeground="black")
Button2.configure(background="#d9d9d9")
Button2.configure(compound='left')
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text="Extract Text")
Button2.configure(command=lambda: (GetText(Entry1.get())))
Text1 = Text(window)
Text1.place(relx=0.033, rely=0.267, relheight=0.431, relwidth=0.923)
Text1.configure(background="white")
Text1.configure(cursor="fleur")
Text1.configure(font="TkTextFont")
Text1.configure(foreground="black")
Text1.configure(highlightbackground="#d9d9d9")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="black")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(wrap="word")
Button3 = Button(window)
Button3.place(relx=0.5, rely=0.733, height=44, width=267)
Button3.configure(activebackground="beige")
Button3.configure(activeforeground="black")
Button3.configure(background="#d9d9d9")
Button3.configure(compound='left')
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text="Read Instructions")
Button3.configure(command=readInstructions)

if __name__ == "__main__":
    window.mainloop()