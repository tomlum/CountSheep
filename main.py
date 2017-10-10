import numpy as np

# For debugging without pulling all of Keras
loadKeras = True

if loadKeras:
    from keras.models import Sequential
    from keras.layers import Dense, Activation
    from keras.layers import Dropout
    from keras.utils import np_utils

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.image as mpim
import glob

# Model Parameters
epochs = 1000

# Import the Data
batch_in = []
batch_out = []
for i in range(0, 9):
    for filepath in glob.glob("./in/" + str(i) + "/*.jpg"):
        batch_in.insert(len(batch_in), mpim.imread(filepath))
    for filepath in glob.glob("./out/" + str(i) + "/*.jpg"):
        batch_out.insert(len(batch_out), mpim.imread(filepath))
batch_in = np.asarray(batch_in)
batch_out = np.asarray(batch_out)

batch_in = batch_in.reshape(-1, 784)
batch_out = batch_out.reshape(-1, 784)
batch_in = batch_in / 255
batch_out = batch_out / 255

im_test = batch_in[1]

# The Model
if loadKeras:
    model = Sequential([
        Dense(32, input_shape=(784,)),
        Activation("relu"),
        Dense(784),
        Activation("relu")
    ])

    model.compile(loss="mean_squared_error",
                  optimizer="adam", metrics=["accuracy"])

    model.fit(batch_in, batch_out, epochs=epochs, batch_size=10, verbose=2)
    scores = model.evaluate(batch_in, batch_out, verbose=0)

#First Seed/Base Prediction
prediction = im_test.reshape(28, 28)

# Interact with the NN
def interact(event):

    global prediction

    if event.key == 'right':
        # Generate/Predict the next number
        prediction = model.predict(
            prediction.reshape(-1, 784)).reshape(28, 28)
        plt.imshow(prediction)
        print("Generating Next Image")
        fig.canvas.draw()

    else:
        # Reset the seed by pressing a number
        for i in range(0, 9):
            if event.key == str(i):
                prediction = mpim.imread(
                    glob.glob("./in/" + str(i) + "/*.jpg")[1])
                plt.imshow(prediction)
                print("Seed is " + str(i))
                fig.canvas.draw()
                break

# Setup the canvas
fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', interact)
plt.imshow(prediction)
plt.show()