import cv2
import threading
import winsound
import time

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = camera.read()
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 8)

alarm = False
alarm_mode = False

def beep():
    winsound.Beep(2500, 1000)

while True:
    _, frame = camera.read()

    if alarm_mode == True:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        _, threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
        start_frame = frame_bw

        if threshold.sum() > 300:
            alarm = True
            threading.Thread(target=beep).start()
            alarm = False

        cv2.imshow("camera", threshold)

    else:
        cv2.imshow("Camera", frame)

    if cv2.waitKey(30) == ord('a'):
        alarm_mode = not alarm_mode

    if cv2.waitKey(30) == ord('e'):
        alarm_mode = False
        break

camera.release()
cv2.destroyAllWindows()
