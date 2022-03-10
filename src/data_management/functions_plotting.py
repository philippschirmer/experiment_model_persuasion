'''This module collects the different functions that will generate charts with the full financial series 
instead of truncated graphs in a later stage of the game. Full graphs serve as a "resolution" of the persuaders 
and receiver's problem, revealing the ex post correct decision, and illustrating whether the receiver's message was ex post accurate or not.

*Note*: The current version of the functions takes a pandas DataFrame as an argument, but it can be easily adapted to take 
a csv file as a data input.
'''

import numpy as np
import plotly.express as px

import pandas as pd

def gen_model_graphs_full(data, model_space, target_directory, data_name):
    '''Function that generates "model" graphs of the full dataset. 
    
    Args:
    
        data  (pandas DataFrame): dataframe that contains column y with dependent variable and x with time trend.
        
        model_space (list): models for which to fit and draw an individual graph each
        
        target_directory (path): working directory where the files are to be saved.
        
        data_name  (string): name or identifier of dataset for graphs to be created.

    Returns: 

        None. (graph is saved to pre-specified directory, but not returned.)
    '''


  
    for i in model_space:

        shift_point = model_space[i]

        fig = px.line(data, x="Time", 
                            y="Stock price",
                            labels={'number_obs':'Number of Observations', 'runtime':'runtime'},
                            title='Development of a stock price',
                            )
        fig.update_yaxes(range=[0, data["Stock price"].max()+100])
        fig.update_layout(paper_bgcolor='#fff' )
        fig.update_layout(plot_bgcolor='#fff' )

        # Draw vertical line indicating switching point.
        fig.add_shape(type="line",
            xref="x", yref="y",
            x0=shift_point, y0=0, x1=shift_point, y1=data["Stock price"].max()+100,
            line=dict(
                dash = "dot",
                color="Black",
                width=3,
            ),
        )

        fig.add_shape(type="line",
            xref="x", yref="y",
            x0=shift_point, y0=data.iat[shift_point,1], x1=80, y1=data.iat[80,1],
            line=dict(
                color="LightSeaGreen",
                width=3,
            ),
        )

        fig.add_shape(type="line",
            xref="x", yref="y",
            x0=0, y0=data.iat[0,1], x1=shift_point, y1=data.iat[shift_point,1],
            line=dict(
                color="LightSeaGreen",
                width=3,
            ),
        )

        # fig.write_image(wd / "img" / "fig_test_{}.jpg".format(shift_point))

        fig.write_image( target_directory / "model_graph_full_{}_{}.jpg".format(data_name, i))
    return None


def gen_neutral_graphs_full(data, target_directory, data_name):
    '''Function that generates "neutral" graphs of the full dataset.
    
    Args:
        
        data (pandas DataFrame): dataframe that contains column "Stock price" with dep. var. and "Time" as indep. var.
        
        target_directory (path): working directory where the files are to be saved.
        
        data_name (string): name or identifier of dataset for graphs to be created.

    Return: 

        None. (graph is saved to pre-specified directory, but not returned.)
    '''
  
    fig = px.line(data, x="Time", 
                        y="Stock price",
                        labels={'number_obs':'Number of Observations', 'runtime':'runtime'},
                        title='Development of a stock price',
                        )
    fig.update_yaxes(range=[0, data["Stock price"].max()+100])
    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )

    fig.write_image( target_directory / "neutral_graph_full_{}.jpg".format(data_name))
    return None

