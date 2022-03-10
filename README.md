# An Experiment on Model Persuasion | Final project for Effective Programming Practices for Economists
by
Carolina Alvarez and
Philipp Schirmer

## Abstract 

> We develop and implement a novel experimental design to test a theory of model-based
persuasion using the experimental platform [oTree](https://www.otree.org/). To achieve this, we make use Python
and JavaScript code and employ HTML and CSS for the experiment’s visuals. In a game
between a sender and possibly multiple receivers, the sender can access an interactive
toolbox of different model choices that can be used to persuade a receiver. The model
messages contain no new ‘hard’ information, and should hence not move the beliefs of a
fully Bayesian receiver. In a setting that mimics real-life financial chart analysis, we can
test several hypotheses concerned with ‘sense-making’ persuasion by a potentially biased
sender.

## Getting started

We have chosen to use the oTree local test server for testing our application. Please follow these steps to set up all app's 
inputs and run the server:

1. Clone the GitHub repository of the current project in your local machine via:

.. code-block:: console
    
    git clone https://github.com/philippschirmer/experiment_model_persuasion.git

2. Create and activate the environment via:

.. code-block:: console

    conda env create -f environment.yml
    
    conda activate experiment_model_persuasion

    conda develop .

3. In the terminal, run: ``pytask``. This will generate all the necessary plots for the experiment, as well as the related documentation. A detailed description of the different tasks can be found in the documentation file. 

4. To start the server, navigate to the ``exp`` folder of the repository and run ``otree devserver`` in the terminal. Then open the browser to ``http://localhost:8000``, which will direct you to the persuasion game demo.

5. Once in the server, you can test the application by playing the full game for both players.

## Overall structure

* ``src/data_generation``: contains a ``task_get_simulated_data``, which generates simulated datasets of stock prices.

* ``src/data_management``: contains ``task_get_plots``, which produces a set of financial charts with model messages used in the game by the persuader. It also contains ``task_get_neutral_plots``, which generates charts without a model message. Finally, the folder also has a file called ``functions_plotting.py``, which contains functions that will be used in a later stage of the game.

* ``exp``: contains the main file of the project, namely the oTree app ``persuasion``.  
  * ``persuasion`` folder: contains an eponymous oTree app.
    * ``__init__.py``: contains the core python code of the experiment.
    * ``test.py``: contains tests (“bots”) for the experiment.

  * ``_static`` folder: contains static pictures to be used in the experiment.
  * ``settings`` contains the overarching properties of the experiment.

* ``src/documentation/task_documentation.py``: generates documentation in the form of pdf and html files.
* ``src/paper/task_paper``: creates a pdf file with the full research paper.

**Note:** The Experiment on Model Persuasion was created on ``oTree version 5.7.2`` and ``pytask version 0.1.9``. 
