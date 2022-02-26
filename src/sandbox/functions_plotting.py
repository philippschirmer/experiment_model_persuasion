# TODO: Function that generates "neutral" graphs, i.e. graphs that don't have any model message yet
# To be used in the first part of the experiment, where the receiver decides without observing data.

# TODO: Make sure graphs only use partial data that is observable to participants.

import numpy as np
import plotly.express as px

import pandas as pd


def gen_model_graphs_trunc(data, model_space, trunc, wd):
    '''TODO: Function that generates "model" graphs, i.e. graphs that feature a model message.
    To be used in the second part of the experiment, where the receiver decides with observing the model.
    
    Inputs:
        data: 2D np.array of shape 2xT - Y's and X's to be plotted
        model_space: 1D np-array: models for which to fit and draw an individual graph, each
        hyperparams: (optional?) 1D np.array - specifying special settings for the graph generation
        (TBD)
        wd: string - working directory where the files are to be saved.

    Outputs: neutral_graph_`data': picture file with neutral graphs saved to prespecified
    project folder.
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

        fig.write_image(wd + "/img/fig_test_{}.jpg".format(shift_point))
    return None





def gen_model_graphs_full(data, model_space, hyperparams, wd):
    '''TODO: Function that generates "neutral" graphs, i.e. graphs that don't have any model message yet
    To be used in the first part of the experiment, where the receiver decides without observing data.
    
    Inputs:
        data: 2D np.array of shape 2xT - Y's and X's to be plotted
        model_space: 1D np-array: models for which to fit and draw an individual graph, each
        hyperparams: (optional?) 1D np.array - specifying special settings for the graph generation
        (TBD)
        wd: string - working directory where the files are to be saved.

    Outputs: neutral_graph_`data': picture file with neutral graphs saved to prespecified
    project folder.
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

        fig.write_image(wd + "/img/fig_test_{}.jpg".format(shift_point))
    return None



def gen_neutral_graphs_trunc(data, trunc, wd):
    '''TODO: Function that generates "neutral" graphs, i.e. graphs that don't have any model message yet
    To be used in the first part of the experiment, where the receiver decides without observing data.
    
    Inputs:
        data: 2D np.array of shape 2xT - Y's and X's to be plotted
        model_space: 1D np-array: models for which to fit and draw an individual graph, each
        hyperparams: (optional?) 1D np.array - specifying special settings for the graph generation
        (TBD)
        wd: string - working directory where the files are to be saved.

    Outputs: neutral_graph_`data': picture file with neutral graphs saved to prespecified
    project folder.
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


    fig.write_image(wd + "/img/neutral_graph_test.jpg")

    return None



def gen_neutral_graphs_full(data, wd):
    '''TODO: Function that generates "neutral" graphs, i.e. graphs that don't have any model message yet
    To be used in the first part of the experiment, where the receiver decides without observing data.
    
    Inputs:
        data: 2D np.array of shape 2xT - Y's and X's to be plotted
        model_space: 1D np-array: models for which to fit and draw an individual graph, each
        hyperparams: (optional?) 1D np.array - specifying special settings for the graph generation
        (TBD)
        wd: string - working directory where the files are to be saved.

    Outputs: neutral_graph_`data': picture file with neutral graphs saved to prespecified
    project folder.
    '''
  
    fig = px.line(data, x="Time", 
                        y="Stock price",
                        labels={'number_obs':'Number of Observations', 'runtime':'runtime'},
                        title='Development of a stock price',
                        )
    fig.update_yaxes(range=[0, data["Stock price"].max()+100])
    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )


    fig.write_image(wd + "/img/neutral_graph_test.jpg")

    return None

