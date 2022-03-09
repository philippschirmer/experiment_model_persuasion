.. exp:

***************
Experiment
***************

This chapter is concerned with the experiment, which is the main deliverable of this project. 

In the exp-folder, the most important objects are the persuasion folder, the _static folder, and the settings.py file.

The persuasion folder contains what is called an oTree "app", which contains the experiment to be played. 

In the persuasion folder, there are several .html files that contains the templates and Javascript code for the individual pages of 
the experiment, as well as a __init__.py file that contains the core python code of the experiment.

As with any oTree experiment since the recent change to a "no-self" format, the __init__.py file contains
all kinds of information such as about the players constants and FormFields, the player decisions that are to be saved for later evaluation,
 any calculations that are necessary and finally the structure of the experiment.

Unfortunately, it is not easily possible to "outsource" the different components of the __init__.py file into different files,
which is why this file contains by far the most code of the project. Nevertheless, we have ensured the file is structured in a 
consistent way such that it remains accessible. 

Structure of the __init__.py file:





.. _init_py:

_init.py file
===============