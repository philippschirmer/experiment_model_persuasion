.. _introduction:


************
Introduction
************

For the final project in Effective Programming Practices for Economists, we implement a novel experimental
design that aims to provide a better understanding of persuasive communication between agents in a financial 
analysis setting. We use *oTree* (Chen et al 2016), an open-source Python framework for experimental research, to develop a 
proof of concept for a game that tests financial client's reaction to models proposed by a financial advisor.

The purpose of the documentation is to provide a clear understanding of the structure of the project and the 
oTree application. This project is based on a template by von Gaudecker (2019) and uses Pytask (Raabe 2020) to 
create inputs for our application.


.. _getting_started:


Getting started
===============

We have chosen to use the oTree local test server for testing our application. Please follow these steps to set up all app's 
inputs and run the server:

* Clone the GitHub repository of the current project in your local machine via:
    
    ``git clone https://github.com/philippschirmer/experiment_model_persuasion``.

* Create and activate the environment via:

    ``conda env create -f environment.yml``
    
    ``conda activate experiment_model_persuasion``

    ``conda develop .``

* In the terminal, run: ``pytask``. This will generate all the necessary plots for the experiment, as well as the related documentation. A detailed description of the different tasks can be found in the following sections. 

* To start the server, navigate to the ``exp`` folder of the repository and run ``otree devserver`` in the terminal. Then open the browser to ``http://localhost:8000``, which will direct you to the persuasion game demo.

* Once in the server, you can test the application by playing the full game for both players.