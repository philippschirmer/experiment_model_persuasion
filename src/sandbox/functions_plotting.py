# TODO: Function that generates "neutral" graphs, i.e. graphs that don't have any model message yet
# To be used in the first part of the experiment, where the receiver decides without observing data.

# TODO: Does it make sense to do the saving in the 

import numpy as np
import plotly.express as px

import pathlib

#TODO: Those are model graphs still.

def gen_neutral_graphs(data, model_space, hyperparams, wd):
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
        fig.update_layout(paper_bgcolor='#fff' )
        fig.update_layout(plot_bgcolor='#fff' )

        fig.add_shape(type="line",
            xref="x", yref="y",
            x0=shift_point, y0=-100, x1=shift_point, y1=300,
            line=dict(
                color="LightSeaGreen",
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



def gen_model_graphs(data, model_space, hyperparams, par_par_cwd):
    '''TODO: Function that generates model graphs, i.e. graphs that don't have any model message yet
    To be used in the first part of the experiment, where the receiver decides without observing any model.
    
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
        fig.update_layout(paper_bgcolor='#fff' )
        fig.update_layout(plot_bgcolor='#fff' )

        # Add vertical line indicating switching point.
        fig.add_shape(type="line",
            xref="x", yref="y",
            x0=shift_point, y0=-100, x1=shift_point, y1=300,
            line=dict(
                dash="dot",
                color="Black",
                width=2,
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

        fig.write_image(par_par_cwd / "otree_model_persuasion" / "_static" / "persuasion" / "fig_test_{}.jpg".format(shift_point))
    return None
