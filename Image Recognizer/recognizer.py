import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test,y_test) = tf.keras.datasets.cifar10.load_data()

y_train = y_train.reshape(-1)
y_test = y_test.reshape(-1)

X_test = X_test.astype("float32")
X_train = X_train.astype("float32")

X_train /= 255.0
X_test /= 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = (32, 32, 3)),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Dense(3000, activation="relu"),
    tf.keras.layers.Dense(1000, activation="relu"),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer = "SGD" , loss = tf.keras.losses.sparse_categorical_crossentropy, metrics=["accuracy"])
model.fit(X_train, y_train, epochs = 5)

model.save("Simple_Image_Classifier(ANN_MODEL)")