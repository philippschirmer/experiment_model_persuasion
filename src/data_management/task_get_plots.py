import numpy as np
import pandas as pd
import pytask
import plotly.express as px
from src.config import BLD

# T_model = 3
 
# t_list_model = np.arange(0,T_model,1,dtype=int)
# model_space = t_list_model
#model_space = [1,2,3,4]

#test for just 1 data set and 1 figure
#for j in range(1,5): 

# for i in range(80):

#     @pytask.mark.task
#     @pytask.mark.depends_on(BLD / "data/data_1.csv")
#     @pytask.mark.produces(f"model_graph_trunc_1_{i}.jpg")
#     def task_get_plots(depends_on, produces, shift_point=i):
#         data_1 = pd.read_csv(depends_on)

#         #shift_point = i

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

@pytask.mark.parametrize(
    "produces, shift_point",
    [(BLD / "figures/model_graph_trunc_1_0.jpg", 0), (BLD / "figures/model_graph_trunc_1_1.jpg", 1), (BLD / "figures/model_graph_trunc_1_2.jpg", 2)],
)
def task_get_plots(shift_point, produces):
    data_1 = pd.read_csv(depends_on)

    #shift_point = i

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
