from __future__ import print_function
import sys
import numpy as np
import glob
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.image as mpim
# matplotlib.use('TKAgg')

batch_x = []
batch_y = []
for i in range(0,9):
	numsX = np.array([])
	numsY = np.array([])
	for filepath in glob.glob("./in/"+str(i)+"/*.jpg"):
		batch_x.insert(len(batch_x),mpim.imread(filepath))
	for filepath in glob.glob("./out/"+str(i)+"/*.jpg"):
		batch_y.insert(len(batch_y),mpim.imread(filepath))
batch_x = np.asarray(batch_x)
batch_y = np.asarray(batch_y)

# batch_x = batch_x.reshape(-1,784)
# batch_y = batch_y.reshape(-1,784)
batch_x = batch_x/255
batch_y = batch_y/255

im_test = batch_x[1]
im_test2 = batch_x[2]


def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == '1':
        plt.imshow(im_test2)
        fig.canvas.draw()


fig, ax = plt.subplots()
plt.imshow(im_test)
fig.canvas.mpl_connect('key_press_event', press)
plt.show()


# fig, ax = plt.subplots()

# fig.canvas.mpl_connect('key_press_event', press)

# ax.plot(np.random.rand(12), np.random.rand(12), 'go')
# xl = ax.set_xlabel('easy come, easy go')
# ax.set_title('Press a key')
# plt.show()
