import glob
from random import randint
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from keras.models import load_model
matplotlib.use("TKAgg")

# Load the model
model = load_model('save.hdf5')

prediction = mpim.imread("./in/0/img_1.jpg")


# Interact with the NN
def interact(event):
    global prediction

    # Predict the next number
    if event.key == "right":
        prediction = model.predict(
            prediction.reshape(-1, 784)
        ).reshape(28, 28)
        plt.imshow(prediction)
        fig.canvas.draw()

    # Reset the seed by pressing a number
    else:
        for i in range(0, 9):
            if event.key == str(i):
                prediction = mpim.imread(
                    glob.glob("./in/" + str(i) + "/*.jpg")[randint(0, 25)])
                plt.imshow(prediction)
                fig.canvas.draw()
                break


# Setup the canvas
fig, ax = plt.subplots()
fig.canvas.mpl_connect("key_press_event", interact)
plt.imshow(prediction)
plt.show()
