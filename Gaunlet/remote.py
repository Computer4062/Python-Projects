import cv2
import mediapipe as mp
import pyautogui as pag

mouseX = 100
mouseY = 100

dirrections = "1: Up | 2: Down | 3: Right | 4: Left | 0: Click"

camera = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
draw = mp.solutions.drawing_utils
style = mp.solutions.drawing_styles

fingerCoordinates = [(8, 6), (12, 10),  (16, 14), (20, 18)]
thumbCoordinates = (4, 2)

Hands = mp_hands.Hands()

while True:
    _, frame = camera.read()

    img_rbg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = Hands.process(img_rbg)
    hands = result.multi_hand_landmarks

    cv2.rectangle(frame, (0, frame.shape[1]), (frame.shape[0] + 200, frame.shape[1] - 200), (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, dirrections, (frame.shape[0] // 2, frame.shape[1] - 170), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)

    if hands:
        handpoint = []
        for landmark in hands:
            draw.draw_landmarks(frame, landmark, mp_hands.HAND_CONNECTIONS)

        for hand_landmark in hands:
            for landmark, lm in enumerate(hand_landmark.landmark):
                h, w, d = frame.shape
                ch, cw = int(lm.y * h), int(lm.x * w)

                handpoint.append((cw, ch))

        for point in handpoint:
            cv2.circle(frame, point, 5, (0, 255, 0), cv2.FILLED)

        fingercount = 0

        for coordinate in fingerCoordinates:
            if handpoint[coordinate[0]][1] < handpoint[coordinate[1]][1]:
                fingercount += 1

        cv2.putText(frame, str(fingercount), (10, frame.shape[1] - 170), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        if fingercount == 0:
            pag.click()

        elif fingercount == 1:
            if mouseY != 0: mouseY -= 5
            pag.moveTo(mouseX, mouseY)

        elif fingercount == 2:
            if mouseY != 2000: mouseY += 5
            pag.moveTo(mouseX, mouseY)

        elif fingercount == 3:
            if mouseX != 2000: mouseX += 5
            pag.moveTo(mouseX, mouseY)

        elif fingercount == 4:
            if mouseX != 0: mouseX -= 5
            pag.moveTo(mouseX, mouseY)

    cv2.imshow("window controller", frame)

    if cv2.waitKey(1) == ord('e'):
        break

cv2.destroyAllWindows()
camera.release()