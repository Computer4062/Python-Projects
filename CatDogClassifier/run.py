import keras
from numpy import argmax, expand_dims
import matplotlib.pyplot as plt

test_data_dir = 'path_to_testing_data_directory'
test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255)
image_size = (128, 128)  # Adjust the image size according to your preference

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=image_size,
    batch_size=32,
    class_mode='binary'  # create each label to a binary-like format
)

model = keras.models.load_model('cat_dog_classifier.h5')

image, label = test_generator[0]  # Get the first image and its label
prediction = model.predict(expand_dims(image, 0))
predicted = round(prediction)

labels = ['cat', 'dog']

print(f'> Actual: {labels[int(label)]}')
print(f'> Predicted: {labels[predicted]}')

plt.imshow(image)
plt.show()
