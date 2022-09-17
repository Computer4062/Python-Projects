import cv2
import os

path = "face_haracascade.xml"

path = cv2.CascadeClassifier(path)

camera = cv2.VideoCapture(0)
originalFaces = 0

while True:
	_, frame = camera.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = path.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)
		facesDetected = len(faces)

		if originalFaces > facesDetected:
			os.startfile('speech.py')

		originalFaces = facesDetected

		cv2.putText(frame,f'faces found = {str(facesDetected)}',(50,50),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
		cv2.imshow("Object Detector", frame)

	if cv2.waitKey(1) == ord('q'):
		break

camera.release()
cv2.destroyAllWindows()