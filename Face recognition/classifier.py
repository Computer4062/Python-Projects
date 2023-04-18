import os
import numpy as np
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "temp")

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')

count = -1
character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for root, dirs, files in os.walk(image_dir):
    for file in files:
        count += 1

        if file.endswith('jpg'):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "_").lower()
            print(path)

        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(image, scaleFactor = 1.5, minNeighbors = 5)

        for (x, y, w, h) in faces:
            roi = image[y: y + h, x: x + w]
            cv2.imwrite(f"D:/Mihan/Python-project-programmes/pythonProjects/Algorithm/ImageComparison/img/{count + 1}.jpg", roi)

        cv2.imshow('image', roi)
        cv2.waitKey(0)

