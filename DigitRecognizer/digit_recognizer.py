import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tkinter import*
import numpy as np
import cv2
import os

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = keras.utils.normalize(x_train)
x_test = keras.utils.normalize(x_test)

#model = keras.models.Sequnetial([
#    keras.layers.Flatten(input_shape=(28,28))
#    keras.layers.Dense(128, activation='relu')
#    keras.layers.Dense(128, activation='relu')
#    keras.layers.Dense(10, activation='softmax')
#])

#model.compile(optimizer='adam', loss='sparse_categorial_crossentropy', metrics=['accuracy'])
#model.fit(x_train, y_train, epochs=3)

#model.save("handwrittern_Digit_recognizer.model")

win = Tk()
win.title("AI number guesser")
filename = ""

def btnFunction(textbox, filename):
    filename = textbox.get()
    model = tf.keras.models.load_model('handwrittern_Digit_recognizer.model')

    loss, accuracy = model.evaluate(x_test, y_test)
    print(f"loss: {loss}, accuracy: {accuracy}")

    try:
        im = cv2.imread(filename)  # open the image
        img = cv2.resize(im, (28, 28), interpolation=cv2.INTER_AREA)[:, :, 0]  # resize the image
        img_array = np.invert(np.array([img]))
        prediction = model.predict(img_array)
        print(f"the number is probably a: {np.argmax(prediction)}")
        converted_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        plt.imshow(converted_img)
        plt.show()

        input("Press the enter key to exit...")
    except:
        print("Error!")

def draw():
    os.system('cmd /c "mspaint" ')

l1 = Label(text="Draw the number, save the file, and enter the file name, then press the enter button to let the AI guess the number")
l1.pack()
textbox = Entry()
textbox.pack()
draw_btn = Button(text="Draw", command=draw)
draw_btn.pack()
btn = Button(text="Enter", command=lambda:btnFunction(textbox, filename))
btn.pack()

win.mainloop()
