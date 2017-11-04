# CountSheep

![](https://thumbs.gfycat.com/RashMadeupAlpineroadguidetigerbeetle-size_restricted.gif)

A proof of concept for Deep Sleep Walk, CountSheep learns to look at an mnist digit and draw the next mnist digit.  Of course, in the process of trying to draw an image from just neural memories, CountSheep distorts its reinterpritation in sometimes chaotic and sometimes meaningful ways.

# Installation
To begin counting sheep you'll just need to install Python 3 and [Pipenv](https://github.com/kennethreitz/pipenv) which keeps track of the dependent libraries.  To install them, just run
`pipenv install`
then to begin, run
`pipenv run python main.py`

note: most mac's might run into [this problem](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python) settuping up the dependencies.

# Controls

* **0-9** reset the initial seed number to be 0 to 9
* **->** Generate the next digit
