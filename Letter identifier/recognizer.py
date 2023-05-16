import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.datasets import emnist
import cv2

emnist = emnist
(x_train, y_train), (x_test, y_test) = emnist.load_data()

x_train = x_train.reshape(x_train.shape[0], 32).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 32).astype('float32')

#normalizing
x_train /= 255
y_train /= 255

#27 outputs
Number_Classes = 27
batch_size = 64
epochs = 20

shape = (32, 32, 1) #row column bitdepth

# initialize model

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(Number_Classes, activation='softmax'))

model.compile(
    loss=keras.losses.categorical_crossentropy,
    optimizer=keras.optimizers.Adadelta(),
    metrics=['accuracy']
)

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)

score = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.save("handwrittern_letter_recognizer.model")