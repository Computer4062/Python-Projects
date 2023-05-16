import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model("handwrittern_letter_recognizer.model")

img = cv2.imread("image.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_array = np.invert(np.array([img]))
prediction = model.predict(img_array)

print(f">{np.argmax(prediction)}")
