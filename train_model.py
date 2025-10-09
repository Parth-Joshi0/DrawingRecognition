import numpy as np
import struct
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models

#Function to load the Images
def load_images(filename):
    with open(filename, "rb") as f:
        #Read Magic Numbers and Dimensions
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        #Read rest of the data
        data = np.frombuffer(f.read(), dtype=np.uint8)
        images = data.reshape(num, rows, cols)
    return images

#function to load the Labels
def load_labels(filenames):
    with open(filenames, "rb") as f:
        magic, num = struct.unpack(">II", f.read(8))
        labels = np.frombuffer(f.read(), dtype=np.uint8)
    return labels

#Loading the Mnist Files
training_images = load_images("mnist/train-images.idx3-ubyte")
training_labels = load_labels("mnist/train-labels.idx1-ubyte")
testing_images = load_images("mnist/t10k-images.idx3-ubyte")
testing_labels = load_labels("mnist/t10k-labels.idx1-ubyte")

#Normalizing Pixel values to 0-1
training_images = training_images.astype(np.float32)/255.0
testing_images = testing_images.astype(np.float32)/255.0

#Reshaping for CNN input
training_images = training_images.reshape(-1, 28, 28, 1)
testing_images = testing_images.reshape(-1, 28, 28, 1)

#Testing if data loaded
#plt.imshow(testing_images[0].reshape(28,28), cmap="gray")
#plt.title(f"Number: {testing_labels[0]}")
#plt.show()

#Building Model
model = models.Sequential([
    layers.Conv2D(64, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])

#Compiling Model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

#Training Model
model.fit(training_images, training_labels, epochs=12, validation_data=(testing_images, testing_labels))

#Testing Model
loss, acc = model.evaluate(testing_images, testing_labels)
print(f"Test Accuracy: {acc*100:.2f}%")

#Saving Model
model.save("digital_model.keras")
print("Model Saved")