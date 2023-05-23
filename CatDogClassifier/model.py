from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load the dataset
# Make sure you have your dataset properly organized in separate folders for cats and dogs
train_data_dir = 'path_to_training_data_directory'
test_data_dir = 'path_to_testing_data_directory'
image_size = (128, 128)  # Adjust the image size according to your preference

# Preprocess the images and generate batches of augmented data
train_datagen = keras.preprocessing.image.ImageDataGenerator(
    rescale=1.0 / 255,  # Normalize pixel values between 0 and 1
    shear_range=0.2,  # Apply shear transformations
    zoom_range=0.2,  # Apply zoom transformations
    horizontal_flip=True  # Flip images horizontally
)

test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255)

# Generate training data
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size, #(128, 128) this will automaticly resize the images
    batch_size=32,
    class_mode='binary' #2 classes
)

# Generate testing data
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=image_size, #(128, 128) this will automaticly resize the images
    batch_size=32,
    class_mode='binary' #2 classes
)

#0 represent a cat
#1 represent a dog

# Build the neural network model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=10,
    validation_data=test_generator,
    validation_steps=test_generator.samples // test_generator.batch_size
)

# Save the model
model.save('cat_dog_classifier.h5')