import sys
import os.path
import glob
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam
from keras.models import load_model
import matplotlib.image as mpim

learningRate = .001


def main(epochs):

    # Import the data
    batch_in = []
    batch_out = []
    for i in range(0, 9):
        for filepath in glob.glob("./in/" + str(i) + "/*.jpg"):
            batch_in.insert(len(batch_in), mpim.imread(filepath))
        for filepath in glob.glob("./out/" + str(i) + "/*.jpg"):
            batch_out.insert(len(batch_out), mpim.imread(filepath))

    # Reshape the data
    batch_in = np.asarray(batch_in)
    batch_out = np.asarray(batch_out)
    batch_in = batch_in.reshape(-1, 784)
    batch_out = batch_out.reshape(-1, 784)
    batch_in = batch_in / 255
    batch_out = batch_out / 255

    # Load the model if a save exists
    if os.path.isfile("./save.hdf5"):
        print("Loading Model...")
        model = load_model("./save.hdf5")

    # Otherwise start from scratch
    else:
        model = Sequential([
            Dense(32, input_shape=(784,)),
            Activation("relu"),
            Dense(784),
            Activation("relu")
        ])

        model.compile(loss="mean_squared_error",
                      optimizer=Adam(lr=learningRate),
                      metrics=["accuracy"])

    # Train the model
    model.fit(
        batch_in,
        batch_out,
        epochs=epochs,
        batch_size=10,
        verbose=0,
        callbacks=[
            ModelCheckpoint(
                filepath="./save.hdf5",
                verbose=1,
                monitor='loss',
                save_best_only=True,
                mode='auto')
        ])


if __name__ == "__main__":
    # Get CLI args
    args = sys.argv

    # Check Args
    if (len(args) < 2 or int(args[1]) < 1):
        print("Invalid number of Epochs")
        print("Command should look like:")
        print("'train.py <# of epochs>'")
        validArgs = False
    else:
        main(int(args[1]))
