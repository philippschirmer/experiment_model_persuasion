.. _data_management:

***************
Data management
***************

This chapter contains the documentation of the code in *src/data_management*. First, the folder contains the tasks that
generate the financial charts showed in the experiment by both persuaders and receivers. 

.. automodule:: src.data_management.task_get_plots
    :members:

.. automodule:: src.data_management.task_get_neutral_plots
    :members:

Secondly, the folder contains the file *functions_plotting:*

.. automodule:: src.data_management.functions_plotting
    :members:


*Note*: As oTree requires the generated pictures to be in the same folder as the app, (i.e. in exp), they are not saved
to the general *bld* folder, but to the *exp/_static/bld* folder.

*Note2*: There appears to be a pytask error related to the plotting tasks that can be resolved by running the tasks a second time to be successful.
This error occurred on a Windows 10 machine. 

*Note3*: Instead of using the pytask.mark.parametrize decorator to generate multiple graphs, we would have preferred to implement a loop over
the task. While already in the Pytask documentation, this will only be supported with pytask 0.2.0, not available at the time of writing
(March 7, 2022). 