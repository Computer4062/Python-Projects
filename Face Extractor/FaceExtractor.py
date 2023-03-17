import os
import numpy as np
import cv2

class GetData:
    def __init__(self):
        self.x_labels = np.array([])
        self.y_train = np.array([])
        self.images = []
        self.labels = []
    def UnPack(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(BASE_DIR, "images")

        face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')

        current_id = 0
        label_ids = {}

        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith('png') or file.endswith('jpg'):
                    path = os.path.join(root, file)
                    label = os.path.basename(os.path.dirname(path)).replace(" ","_").lower()

                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1

                    #verify image, turn to numpy array, convert to grey color

                    image = cv2.imread(path) #convert to gray
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    faces = face_cascade.detectMultiScale(image, scaleFactor = 1.5, minNeighbors = 5)

                    for (x, y, w, h) in faces:
                        roi = image[y: y+h, x: x+w]
                        self.images.append(roi)
                        self.labels.append(label_ids)

        return self.images, self.labels












