# Description: functions_plotting collects the different functions that generate graphs for both senders and receivers
# in the model persuasion experiment.

import numpy as np
import plotly.express as px

import pandas as pd


def gen_model_graphs_trunc(data, model_space, trunc, target_directory, data_name):
    '''Function generates graphs of truncated dataset that contain a model message.
    Using truncated data, the function iterates over the model space, generating one graph per possible model. 
    The function constructs the graphs and rescales data automatically, before saving the files to the specified directory.
    In the current form, the model_space is the possible switching point of the time trend, and the fitted model 
    is a naive linear estimation of the trend before and after the switching point. 

    Truncated model graphs are the central object of choice for the persuader, who picks for a given data a model message.
    The chosen graph is then sent to the receiver, who makes an investment decision based on the presented graph with model.
    
    Inputs:
        data: pandas DataFrame - dataframe that contains column y with dependent variable and x with time trend.
        model_space: list or list-like: models for which to fit and draw an individual graph each
        trunc: integer - truncation point determining how much of the data participants observe.
        target_directory: path - working directory where the files are to be saved.
        data_name:  string - name or identifier of dataset for graphs to be created.

    Outputs: None. (graph is saved to pre-specified directory, but not returned.)
    '''



  
    for i in model_space:

        shift_point = model_space[i]

        fig = px.line(data.head(trunc), x="Time", 
                            y="Stock price",
                            labels={'number_obs':'Number of Observations', 'runtime':'runtime'},
                            title='Development of a stock price',
                            )
        fig.update_layout(paper_bgcolor='#fff' )
        fig.update_layout(plot_bgcolor='#fff' )
        fig.update_yaxes(range=[0, data["Stock price"].max()+100])
        fig.update_xaxes(range=[0, trunc+20])

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

        fig.write_image( target_directory / "model_graph_trunc_{}_{}.jpg".format(data_name, i))
    return None





def gen_model_graphs_full(data, model_space, target_directory, data_name):
    '''Function that generates "model" graphs of the full dataset, i.e. graphs that contain a model message.
    Function iterates over the model space, generating one graph per possible model. 
    The function constructs the graphs and rescales data automatically, before saving the files to the specified directory.
    In the current form, the model_space s the possible switching point of the time trend, and the fitted model 
    is a naive linear estimation of the trend before and after the switching point. 

    Full graphs serve as a "resolution" of the persuaders and receiver's problem, revealing the ex post correct decision,
    and illustrating whether the receiver's message was ex post accurate or not.
    
    Inputs:
        data: pandas DataFrame - dataframe that contains column y with dependent variable and x with time trend.
        model_space: list or list-like: models for which to fit and draw an individual graph each
        target_directory: path - working directory where the files are to be saved.
        data_name:  string - name or identifier of dataset for graphs to be created.

    Outputs: None. (graph is saved to pre-specified directory, but not returned.)
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



def gen_neutral_graphs_trunc(data, trunc, target_directory, data_name):
    '''Function that generates "neutral" graphs, i.e. graphs that don't feature a model message.
    The function constructs the graphs using truncated columns of the DataFrame and rescales data automatically,
    before saving the files to the specified directory.

    To be used in the first part of the experiment, where the receiver decides without observing data.
    
    Inputs:
        data: pandas DataFrame - dataframe that contains column y with dependent variable and x with time trend.
        trunc: integer - truncation point determining how much of the data participants observe.
        target_directory: path - working directory where the files are to be saved.
        data_name:  string - name or identifier of dataset for graphs to be created.

    Outputs: None. (graph is saved to target_directory, but not returned.)
    '''





  
    fig = px.line(data.head(trunc), x="Time", 
                        y="Stock price",
                        labels={'number_obs':'Number of Observations', 'runtime':'runtime'},
                        title='Development of a stock price',
                        )
    fig.update_yaxes(range=[0, data["Stock price"].max()+100])
    fig.update_xaxes(range=[0, trunc+20])
    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )


    fig.write_image( target_directory / "neutral_graph_trunc_{}.jpg".format(data_name))
    return None



def gen_neutral_graphs_full(data, target_directory, data_name):
    '''Function that generates "neutral" graphs of the full dataset, i.e. graphs that don't feature a model message.
    The function constructs the graphs and rescales data automatically, before saving the files to the specified directory.
    Graphs serve as a "resolution" of the receiver's problem, revealing the expost price and correct decision.
    
    Inputs:
        data: pandas DataFrame - dataframe that contains column "Stock price" with dep. var. and "Time" as indep. var.
        target_directory: path - working directory where the files are to be saved.
        data_name:  string - name or identifier of dataset for graphs to be created.

    Outputs: None. (graph is saved to pre-specified directory, but not returned.)
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

