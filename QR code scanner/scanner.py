from pyzbar import pyzbar
import cv2
from tkinter import messagebox

camera = cv2.VideoCapture(0)
read = False #prevent window spamming
first_clip = False
while True:
    _, frame = camera.read()

    #convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #find the amount of QR codes
    qr_codes = pyzbar.decode(gray)
    if qr_codes and first_clip:
        for qr_code in qr_codes:
            (x, y, w, h) = qr_code.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #binary to string
            data = qr_code.data.decode('utf-8')
            #show message in a seperate window
            if not read:
                messagebox.showinfo('QR code data', data)
                read = True

    cv2.imshow('QR scanner', frame)
    if cv2.waitKey(1) ==ord('q'):
        break

    first_clip = True

cv2.destroyAllWindows()
camera.release()