# [CountSheep](https://www.tomlum.com/doodlebrains)

![](https://thumbs.gfycat.com/RashMadeupAlpineroadguidetigerbeetle-size_restricted.gif)

CountSheep learns to look at an mnist digit and draw the next mnist digit counting upwards.  Of course, in the process of trying to draw an image from just neural memories, CountSheep distorts its reinterpritation in sometimes chaotic and sometimes meaningful ways.

To try CountSheep for yourself and learn more about it, check out [Doodle Brains](https://www.tomlum.com/doodlebrains).

# Installation
To begin counting sheep you'll just need to install Python 3 and [Pipenv](https://github.com/kennethreitz/pipenv) which keeps track of the dependent libraries.  To install them, just run
`pipenv install`

note: some mac's might run into [this problem](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python) setting up the dependencies.

# Training & Generating
To start training the network, run
`pipenv run python train.py <Number of Epochs to Train>`
To watch the network generate numbers, run
`pipenv run python count.py`

# Controls

* **0-9** reset the initial seed number to be 0 to 9
* **->** Generate the next digit
