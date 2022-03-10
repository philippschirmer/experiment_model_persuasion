.. exp:

***************
Experiment
***************

The *exp* folder contains the main deliverable of this project, namely the **oTree** app *persuasion* that is
the experiment for model persuasion.

In the *exp* folder, the most important objects are the *persuasion* folder, the *_static* folder, and the *settings.py* file.

*   The *persuasion folder* contains an eponymous oTree app.
*   The *_static* folder contains static pictures to be used in the experiment: The folder is populated by the tasks that
    generate the pictures, which are then accessed by the Javascript in the .html files.
*   The *settings* file contains the overarching properties of the experiment. for example whether it is to be hosted in a 
    room (which would be necessary for a "real" monetized experiment), how many participants are participating in the experiment,
    and whether the experiment is to be played by bots (which is akin to running tests for the experiment).




Structure of the *persuasion* folder
########

In the *persuasion* folder, there are

*   .html-files such as *Introduction.html* that contain the templates and Javascript code for the individual pages of the experiment,
*   a *tests.py* file that contains tests ("bots") for the experiment as well as a
*   *__init__.py* file that contains the core python code of the experiment.

As with any oTree experiment since the recent change to a new "no-self" format, the *__init__.py* file contains
all kinds of information such as about the Player class with constants and FormFields, the player decisions that are to be saved for later evaluation,
any calculations that are necessary and finally the structure of the experiment.

Unfortunately, it is not easily possible to "outsource" the different components of the *__init__.py* file into different files,
which is why this file contains by far the most code of the project. Nevertheless, we have ensured the file is structured in a 
consistent way such that it remains accessible. 

Contents of the *__init__.py* file:
**********************

The *__init__.py* file contains, in this order,

*   the *BaseConstants* class, defining the number of players per group, rounds played and show-up-fee.
*   the *Player* class, which contains all fields to be filled throught the experiment, and which are saved
    in a model for later analysis (e.g. of treatment effects)
*   functions that are called during the experiment, e.g sending a message or
    for calculating payoffs.
*   classes for all pages of the experiment, which define which fields a player has to fill in,
    which functions should be called when, and which variables from the Python "model" are transmitted to
    the JavaScript / html
*   the *page_sequence* list, which defines the sequence in which pages are shown

Given the length of the *__init__.py* file, it is not possible to describe the contents in detail.

For changing general attributes of the game, it should suffice to change  some of the BaseConstant at the beginning of the *__init__.py* file.
Maybe most importantly, when increasing the number of players in *settings.py* file, it might be necessary to also adjust the PLAYERS_PER_GROUP constant.

Page templates and JavaScript
**********************

The majority of files in the *persuasion* folder are .hmtl files that contain the templates for pages, and the
JavaScript code required to run the experiment. For example, *PersuaderPage.html* contains the information page for a persuader,
and PersuaderDecision.html the code for presenting a receiver with his choices.

Where possible we employed the same .html template for several pages. For example, each of the five model choices
the persuader makes stem from a single template *DecisionPersuader.html* that is reused.

The page templates differ in complexity, where some employ only basic html, while others make use of
CSS style commands and more complex JavaScript code that interacts with the Python code base.
An example for a more complex template is *DecisionPersuader.html*. We employ style commands to design a slider, and html
include a model graph and the slider. Then, using JavaScript, we coded an "EventListener" that tracks user interaction with the slider,
and changes the model graph accordingly. When the persuader is ready to send a message, leaving the page saves the chosen message to the Python model.
To reuse the template for different choice pages, we employ a Python script in the *__init__.py* for example in class *DecisionPersuader1.html*, passing the subset of graphs to the JavaScript.




Tests.py - Bot-based testing 
**********************

*tests.py* contains the testing procedure for the experiment. Testing the correct functioning of
an experiment is different from testing individual functions to the degree that it relies on testing 
the correct behavior of the objects in addition to some of the functions that are used. To ensure an experiment doesn't have flaws that might lead to unexpected behavior for the user,
we wrote a "bot" that takes the role of real participants, takes actions and fills out forms.

The PlayerBot in tests.py moves through the pages of the experiment and enters unacceptable answers. We check
whether these unacceptable answers correctly prompts error messages, before advancing the bot using valid answers.

Finally, we also check whether basic functions such as the calculation of payoffs yield the desired values.

In addition to the bot testing, we also manually tested our experiment extensively. 


Interacting with the experiment
===============================

In addition to running the experiment as described in the "getting started" subsection of the Introduction, 
there are some ways to adapt the experiment users might find interesting.

The baseline interaction is to host the game as is on a local server, start a session and
navigate oneself through both the persuader and receiver role. This allows to get a good feeling
for the structure of the experiment we designed, as well as to see both sides of the experiment.

If you are interested in seeing how the testing works, bot-based testing can be enabled by going into the *settings.py* 
file and setting use_browser_bots=True. Then, restarting the session and clicking on a participant link
shows how a bot navigates through the experiment, checking for potential flaws and ensuring correct functioning.

The experiment can also be run with a greater number of players than two, and with a variable group size.
To achieve this, set num_demo_participants>=2. Then, in the *__init__.py* file, adjust
PLAYERS_PER_GROUP as desired, but ensure number of participants is a multiple of the group size.
Please note that in this proof of concept, the info texts don't accurately describe the game of larger group
size yet. However, payoffs are already implemented for any number of partipants and groups size.

Finally, the persuasion app can of course be changed in many different ways. New treatments can be introduced as is 
seen fit. In order to change the graphs that appear in the experiment, it suffices to change the inputs of
*task_get_simulated_data.py*, for example by changing the trend or the seed. Rerunning *pytask* then creates new
images and saves them in the experiment's *_static* folder, so that new runs of the experiment feature different graphs.
