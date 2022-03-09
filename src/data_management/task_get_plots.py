import numpy as np
import pandas as pd
import pytask
import plotly.express as px
from src.config import BLD, EXP

data_sets = 5
models = 81

param_list = [(0,0) for i in range((data_sets)*(models))]

for j in range(1,data_sets+1):
    for i in range(0, models):
        index = models*(j-1) + i
        param_list[index]= (EXP / "_static/bld" / f"model_graph_trunc_{j}_{i}.jpg", BLD / f"data/data_{j}.csv", i)


@pytask.mark.task
@pytask.mark.parametrize(
"produces, depends_on, shift_point",
param_list,)

def task_get_plots(produces, depends_on, shift_point):
    '''Task that generates the financial graphs picked by the persuader and later sent to the receiver.
    Using truncated data, a naiver linear estimation of the trend is fitted before and after 
    each possible switching point. The task then creates a graph per possible model, generating a full set 
    of charts that are displayed by a javascript slider in the oTree application.

    Args:
    
        produces (path): path to export financial chart in the form of a jpg image.

        depends_on (path): path where the data.csv file can be found.

        shift_point (integer): point in the x-axis from where the model will be fitted.

    Returns: None. (graph is saved to pre-specified directory, but not returned.)
    '''
    data_1 = pd.read_csv(depends_on)

    fig = px.line(data_1.head(80), x="Time", 
                        y="Stock price",
                        labels={'number_obs':'Number of Observations', 'runtime':'runtime'},
                        title='Development of a stock price',
                        )
    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )
    fig.update_yaxes(range=[0, data_1["Stock price"].max()+100])
    fig.update_xaxes(range=[0, 80+20])

    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=shift_point, y0=0, x1=shift_point, y1=data_1["Stock price"].max()+100,
        line=dict(
            dash = "dot",
            color="Black",
            width=3,
        ),
    )

    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=shift_point, y0=data_1.iat[shift_point,1], x1=80, y1=data_1.iat[80,1],
        line=dict(
            color="LightSeaGreen",
            width=3,
        ),
    )

    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=0, y0=data_1.iat[0,1], x1=shift_point, y1=data_1.iat[shift_point,1],
        line=dict(
            color="LightSeaGreen",
            width=3,
        ),
    )
    fig.write_image(produces)


# Code that only works under new pytask 0.2.0 (not released yet as of March 6 2022)

# for i in range(5):

#     @pytask.mark.task
#     @pytask.mark.depends_on(BLD / "data/data_1.csv")
#     @pytask.mark.produces(BLD / "figures" / "model_graph_trunc_1_{}.jpg".format(i))
#     def task_get_plots(produces, depends_on):
#         data_1 = pd.read_csv(depends_on)

#         shift_point = i
#         'test'
#         fig = px.line(data_1.head(80), x="Time", 
#                             y="Stock price",
#                             labels={'number_obs':'Number of Observations', 'runtime':'runtime'},
#                             title='Development of a stock price',
#                             )
#         fig.update_layout(paper_bgcolor='#fff' )
#         fig.update_layout(plot_bgcolor='#fff' )
#         fig.update_yaxes(range=[0, data_1["Stock price"].max()+100])
#         fig.update_xaxes(range=[0, 80+20])

#         fig.add_shape(type="line",
#             xref="x", yref="y",
#             x0=shift_point, y0=0, x1=shift_point, y1=data_1["Stock price"].max()+100,
#             line=dict(
#                 dash = "dot",
#                 color="Black",
#                 width=3,
#             ),
#         )

#         fig.add_shape(type="line",
#             xref="x", yref="y",
#             x0=shift_point, y0=data_1.iat[shift_point,1], x1=80, y1=data_1.iat[80,1],
#             line=dict(
#                 color="LightSeaGreen",
#                 width=3,
#             ),
#         )

#         fig.add_shape(type="line",
#             xref="x", yref="y",
#             x0=0, y0=data_1.iat[0,1], x1=shift_point, y1=data_1.iat[shift_point,1],
#             line=dict(
#                 color="LightSeaGreen",
#                 width=3,
#             ),
#         )
#         fig.write_image(produces)




