import cv2
import imutils
import threading
import winsound

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = camera.read()
state_frame = imutils.resize(start_frame, width = 500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 8)

alarm = False
alarm_mode = False

def beep():
    winsound.Beep(2500, 1000)

while True:
    _, frame = camera.read()
    frame = imutils.resize(frame, width = 500)

    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlue(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshhold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw

        if threshold.sum() > 300:
            alarm = True

        cv2.imshow("camera", threshold)

    else:
        cv2.imshow("Camera", frame)

    if alarm and alarm_mode:
        threading.Thread(target = beep).start()
        alarm = False

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord('t'):
        alarm_mode = not alarm_mode

    if key_pressed == ord('e'):
        alarm_mode = False
        break

camera.release()
cv2.destroyAllWindows()