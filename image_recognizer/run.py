import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model("cnn - image_classifier")

classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

img = cv2.imread("image.png")
img = cv2.resize(img, (32, 32), cv2.INTER_AREA)
img_array = np.invert(np.array([img]))
prediction = model.predict(img_array)

value = ""

for i in range(len(classes)):
    if np.argmax(prediction) - 1 == i:
        value = classes[i]
        break

print(f"predict: {value}")