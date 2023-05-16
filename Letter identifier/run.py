import matplotlib.pyplot as plt
from keras.datasets import emnist
import numpy as np

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

(x_train, y_train), (x_test, y_test) = emnist.load_data()

image_index = 42
selected_image = x_train[image_index]

plt.imshow(selected_image, cmap='gray')
plt.show()

prediction = model.predict(selected_image)
predicted = np.argmax(prediction)

print(f">{alphabet[predicted]}")
