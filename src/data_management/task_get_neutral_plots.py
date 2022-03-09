import pandas as pd
import pytask
import plotly.express as px
from src.config import BLD, EXP


# task for neutral graphs

data_sets = 5

param_list_neutral = [(0,0) for i in range((data_sets))]

for j in range(1,data_sets+1):
    index = j-1
    param_list_neutral[index]= (EXP / "_static/bld" / f"neutral_graph_trunc_{j}.jpg", BLD / f"data/data_{j}.csv")

@pytask.mark.task
@pytask.mark.parametrize(
"produces, depends_on",
param_list_neutral,) 

def task_get_neutral_plots(produces, depends_on):
    '''Task that generates neutral graphs (i.e., without model messages) from truncated data. These graphs
    are shown to the receivers so they make financial decisions prior to the exposure to model messages send
    by the persuader.

    Args:

        produces (path): path to export neutral financial chart in the form of a jpg image.

        depends_on (path): path where the data.csv file can be found.

    '''
    data = pd.read_csv(depends_on)
    trunc = 80
    fig = px.line(data.head(trunc), x="Time", 
                        y="Stock price",
                        labels={'number_obs':'Number of Observations', 'runtime':'runtime'},
                        title='Development of a stock price',
                        )
    fig.update_yaxes(range=[0, data["Stock price"].max()+100])
    fig.update_xaxes(range=[0, trunc+20])
    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )


    fig.write_image(produces)



