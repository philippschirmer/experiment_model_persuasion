
import pandas as pd

import numpy as np

import pytask
import plotly.express as px

import plotly.graph_objects as go

import math


def gen_graphs_neutral(data, symbol, start, hist_length, pred_length, model):
    '''
    Function that generates plots for the real data application. 
    Args:
    TODO
    '''

    # TODO normalize the price to be 100 at end of observed history.

    # TODO: Don't need data_hist, just a subset of data_hist_pred
    # data_hist = data.iloc[start:start+hist_length]

    data_hist_pred = data.iloc[start: start + hist_length + pred_length].copy()

    # Reset the index of the dataframe to "anonymize" time.
    data_hist_pred.reset_index(drop=True, inplace=True)


    norm_price = data_hist_pred[symbol].iloc[hist_length]

    #data_hist_pred[symbol] = df[symbol].apply(lambda x: x*100/ norm_price)
    data_hist_pred[symbol] = (data_hist_pred[symbol] * 100 / data_hist_pred[symbol].iloc[hist_length])

    # print(data_hist_pred[symbol].iloc[hist_length + 1])

    # print(data_hist_pred.iloc[hist_length - 2 : hist_length+2])



    # subset of data that contains the "history"
    #data_hist= data_hist_pred.iloc[0: hist_length]
    data_hist= data_hist_pred.iloc[0:hist_length].copy()

    hist_max = data_hist[symbol].max()
    hist_min = data_hist[symbol].min()

    # print(hist_max)

    # TODO: Can make this much more beautiful here.


    #fig = px.line(data.iloc[start:start+hist_length], x="Time",
    fig = px.line(data_hist_pred.iloc[0:hist_length], x=data_hist_pred.iloc[0:hist_length].index,
                        y=symbol,
                        title='Development of a stock price',
                        )
    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )
    
    fig.update_layout(paper_bgcolor='#fff',
    xaxis_title="Trading Day",
    yaxis_title="Stock price"
    )


    fig.update_yaxes(range=[hist_min - 10 , hist_max + 10])
    fig.update_xaxes(range=[0, hist_length+pred_length])

    fig.write_image("graphs/neutral/" + symbol + str(start) + " " + str(hist_length) + " " + str(pred_length) + " " + model + ".png")

    pass


def gen_graphs_incl_pred(data, symbol, start, hist_length, pred_length, model):
    '''
    Function that generates plots for the real data application. 
    Args:
    TODO
    '''

    # TODO normalize the price to be 100 at end of observed history.

    # TODO: Don't need data_hist, just a subset of data_hist_pred
    # data_hist = data.iloc[start:start+hist_length]

    data_hist_pred = data.iloc[start: start + hist_length + pred_length].copy()

    # Reset the index of the dataframe to "anonymize" time.
    data_hist_pred.reset_index(drop=True, inplace=True)


    norm_price = data_hist_pred[symbol].iloc[hist_length]

    #data_hist_pred[symbol] = df[symbol].apply(lambda x: x*100/ norm_price)
    data_hist_pred[symbol] = (data_hist_pred[symbol] * 100 / data_hist_pred[symbol].iloc[hist_length])

    print(data_hist_pred[symbol].iloc[hist_length + 1])

    print(data_hist_pred.iloc[hist_length - 2 : hist_length+2])



    # subset of data that contains the "history"
    #data_hist= data_hist_pred.iloc[0: hist_length]
    data_hist= data_hist_pred.iloc[0:hist_length].copy()

    hist_max = data_hist[symbol].max()
    hist_min = data_hist[symbol].min()

    print(hist_max)

   # TODO: Can make this much more beautiful here.


    #fig = px.line(data.iloc[start:start+hist_length], x="Time",
    fig = px.line(data_hist_pred.iloc[0:hist_length + pred_length], x=data_hist_pred.iloc[0:hist_length + pred_length].index,
                        y=symbol,
                        title='Development of a stock price',
                        )

    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )
    
    fig.update_yaxes(range=[hist_min - 10 , hist_max + 10])
    fig.update_xaxes(range=[0, hist_length+pred_length])

    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=hist_length, y0=hist_min - 10, x1=hist_length, y1=hist_max + 10,
        line=dict(
            dash = "dot",
            color="Black",
            width=3,
        ),
    )





    fig.write_image("graphs/neutral_hist_pred/" + symbol + str(start) + " " + str(hist_length) + " " + str(pred_length) + " pred " + model + ".png")

    pass





def gen_graphs_two_trends(data, symbol, start, hist_length, pred_length, shift_point):
    '''
    Function that generates plots for the real data application. 

    Generate two trends, one trend from beginning of history until a switching point, another one until end of history +
    prediction time.

    Args:
    TODO
    '''

    # TODO normalize the price to be 100 at end of observed history.

    # TODO: Don't need data_hist, just a subset of data_hist_pred
    # data_hist = data.iloc[start:start+hist_length]

    data_hist_pred = data.iloc[start: start + hist_length + pred_length].copy()

    # Reset the index of the dataframe to "anonymize" time.
    data_hist_pred.reset_index(drop=True, inplace=True)


    norm_price = data_hist_pred[symbol].iloc[hist_length]

    #data_hist_pred[symbol] = df[symbol].apply(lambda x: x*100/ norm_price)
    data_hist_pred[symbol] = (data_hist_pred[symbol] * 100 / data_hist_pred[symbol].iloc[hist_length])

    # print(data_hist_pred[symbol].iloc[hist_length + 1])

    # print(data_hist_pred.iloc[hist_length - 2 : hist_length+2])



    # subset of data that contains the "history"
    #data_hist= data_hist_pred.iloc[0: hist_length]
    data_hist= data_hist_pred.iloc[0:hist_length].copy()

    hist_max = data_hist[symbol].max()
    hist_min = data_hist[symbol].min()

    # print(hist_max)

    # TODO: Can make this much more beautiful here.


    #fig = px.line(data.iloc[start:start+hist_length], x="Time",
    fig = px.line(data_hist_pred.iloc[0:hist_length], x=data_hist_pred.iloc[0:hist_length].index,
                        y=symbol,
                        title='Development of a stock price',
                        )
    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )

    fig.update_layout(paper_bgcolor='#fff',
    xaxis_title="Trading Day",
    yaxis_title="Stock price"
    )

    fig.update_yaxes(range=[hist_min - 10 , hist_max + 10])
    fig.update_xaxes(range=[0, hist_length+pred_length])


    # draw line to mark end of history
    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=hist_length, y0=hist_min - 10, x1=hist_length, y1=hist_max + 10,
        line=dict(
            dash = "dot",
            color="Black",
            width=2,
        ),
    )

    # Draw second trend line. 
    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=shift_point, y0=data_hist_pred[symbol].iloc[shift_point], x1=hist_length, y1=data_hist_pred[symbol].iloc[hist_length],
        line=dict(
            color="LightSeaGreen",
            width=2,
        ),
    )



    
    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=0, y0=data_hist_pred[symbol].iloc[0], x1=shift_point, y1=data_hist_pred[symbol].iloc[shift_point],
        line=dict(
            color="LightSeaGreen",
            width=2,
        ),
    )
    #

    # Calc the implied slope of second model to adjust the fits, draw predictions.

    point_1 = data_hist_pred[symbol].iloc[shift_point]

    trunc_1 = hist_length 

    point_2 = data_hist_pred[symbol].iloc[trunc_1]

    slope = 0
    if hist_length != shift_point:
        slope= (point_2 - point_1) / (trunc_1-shift_point)

    print(slope)

    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=hist_length, y0=point_2, x1=hist_length + pred_length, y1=point_2 + slope * (pred_length),
        line=dict(
            dash = "dot",
            color="LightSeaGreen",
            width=2,
        ),
    )

    # make Shift point more salient.
    #fig.add_traces(
    #    px.scatter(
    #                data_hist_pred[symbol].iloc[shift_point], x=shift_point,
    #                y=symbol).update_traces(marker_size=8, marker_color="LightSeaGreen").data
    #                #data_hist_pred.iloc[hist_length: hist_length+1], x=data_hist_pred.iloc[hist_length: hist_length+1].index,
    #
    #   )

    # TODO: Add circles

    fig.add_trace(go.Scatter(x=[shift_point], y=[data_hist_pred[symbol].iloc[shift_point]])).update_traces(marker_size=8, marker_color="LightSeaGreen").data
    fig.update_layout(showlegend=False)



    # fig.add_shape(type="circle",
    #     xref="x", yref="y",
    #     x0=shift_point-0.1, y0=data_hist_pred.iloc[shift_point]-0.1, x1=shift_point+0.1, y1=data_hist_pred.iloc[shift_point]+0.1,
    #     line_color="LightSeaGreen",
    # )


    fig.write_image("graphs/two_trends/" + symbol + str(start) + " " + str(hist_length) + " " + str(pred_length) + " " + str(shift_point) + ".png")



    pass





def gen_graphs_three_trends(data, symbol, start, hist_length, pred_length, shift_points):
    '''
    Function that generates plots for the real data application. 

    Generate two trends, one trend from beginning of history until a switching point, another one until end of history +
    prediction time.

    Args:
    shift_points: List of integers, indicating the shift points of the linear models
    TODO
    '''

    # TODO normalize the price to be 100 at end of observed history.

    # TODO: Don't need data_hist, just a subset of data_hist_pred
    # data_hist = data.iloc[start:start+hist_length]

    data_hist_pred = data.iloc[start: start + hist_length + pred_length].copy()

    # Reset the index of the dataframe to "anonymize" time.
    data_hist_pred.reset_index(drop=True, inplace=True)


    norm_price = data_hist_pred[symbol].iloc[hist_length]

    #data_hist_pred[symbol] = df[symbol].apply(lambda x: x*100/ norm_price)
    data_hist_pred[symbol] = (data_hist_pred[symbol] * 100 / data_hist_pred[symbol].iloc[hist_length])

    # print(data_hist_pred[symbol].iloc[hist_length + 1])

    # print(data_hist_pred.iloc[hist_length - 2 : hist_length+2])



    # subset of data that contains the "history"
    #data_hist= data_hist_pred.iloc[0: hist_length]
    data_hist= data_hist_pred.iloc[0:hist_length].copy()

    hist_max = data_hist[symbol].max()
    hist_min = data_hist[symbol].min()

    # print(hist_max)

    # TODO: Can make this much more beautiful here.


    #fig = px.line(data.iloc[start:start+hist_length], x="Time",
    fig = px.line(data_hist_pred.iloc[0:hist_length], x=data_hist_pred.iloc[0:hist_length].index,
                        y=symbol,
                        title='Development of a stock price',
                        )
    fig.update_layout(paper_bgcolor='#fff' )
    fig.update_layout(plot_bgcolor='#fff' )
        # 
    fig.update_yaxes(range=[hist_min - 10 , hist_max + 10])
    fig.update_xaxes(range=[0, hist_length+pred_length])


    # draw line to mark end of history
    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=hist_length, y0=hist_min - 10, x1=hist_length, y1=hist_max + 10,
        line=dict(
            dash = "dot",
            color="Black",
            width=2,
        ),
    )

    # Draw the first trend line.
    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=0, y0=data_hist_pred[symbol].iloc[0], x1=shift_points[0], y1=data_hist_pred[symbol].iloc[shift_points[0]],
        line=dict(
            color="LightSeaGreen",
            width=2,
        ),
    )

    # Draw second trend line. 
    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=shift_points[0], y0=data_hist_pred[symbol].iloc[shift_points[0]], x1=shift_points[1], y1=data_hist_pred[symbol].iloc[shift_points[1]],
        line=dict(
            color="LightSeaGreen",
            width=2,
        ),
    )

    # Draw third trend line. 
    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=shift_points[1], y0=data_hist_pred[symbol].iloc[shift_points[1]], x1=hist_length, y1=data_hist_pred[symbol].iloc[hist_length],
        line=dict(
            color="LightSeaGreen",
            width=2,
        ),
    )
   


    #

    # Calc the implied slope of second model to adjust the fits, draw predictions.

    point_1 = data_hist_pred[symbol].iloc[shift_points[1]]

    trunc_1 = hist_length 

    point_2 = data_hist_pred[symbol].iloc[trunc_1]

    slope = 0
    if hist_length != shift_points[1]:
        slope= (point_2 - point_1) / (trunc_1-shift_points[1])

    print(slope)

    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=hist_length, y0=point_2, x1=hist_length + pred_length, y1=point_2 + slope * (pred_length),
        line=dict(
            dash = "dot",
            color="LightSeaGreen",
            width=2,
        ),
    )

    fig.write_image("graphs/three_trends/" + symbol + str(start) + " " + str(hist_length) + " " + str(pred_length) + " " + str(shift_points[0]) + str(shift_points[1]) + ".png")



    pass





def gen_graphs_n_trends(data, symbol, start, hist_length, pred_length, shift_points, show_outcome):
    '''
    Function that generates plots for the real data application, with an arbitrary number of trend changes.



    Generate two trends, one trend from beginning of history until a switching point, another one until end of history +
    prediction time.

    Args:
    shift_points: Ordered List of integers in [0 <i_0 < i_1, ... < i_n <= hist_length], indicating the shift points of the linear models.
                  For an empty list, no model is assumed (neutral graph is produced)

    show_outcome: Boolean: Enable whether the actual development is shown, or just the history 

    TODO
    '''

    data_hist_pred = data.iloc[start: start + hist_length + pred_length +1].copy()

    # Reset the index of the dataframe to "anonymize" time.
    data_hist_pred.reset_index(drop=True, inplace=True)


    norm_price = data_hist_pred[symbol].iloc[hist_length]

    #data_hist_pred[symbol] = df[symbol].apply(lambda x: x*100/ norm_price)
    data_hist_pred[symbol] = (data_hist_pred[symbol] * 100 / data_hist_pred[symbol].iloc[hist_length])

    # print(data_hist_pred[symbol].iloc[hist_length + 1])

    # print(data_hist_pred.iloc[hist_length - 2 : hist_length+2])



    # subset of data that contains the "history"
    #data_hist= data_hist_pred.iloc[0: hist_length]
    data_hist= data_hist_pred.iloc[0:hist_length].copy()

    hist_max = data_hist[symbol].max()
    hist_min = data_hist[symbol].min()

    # print(hist_max)

    # TODO: Can make this much more beautiful here.


    #fig = px.line(data.iloc[start:start+hist_length], x="Time",

    if show_outcome == True:
        fig = px.line(data_hist_pred.iloc[0:hist_length+ pred_length+1], x=data_hist_pred.iloc[0:hist_length+ pred_length+1 ].index,
                            y=symbol,
                            title='Development of a stock price',
                            )

        fig.update_layout(plot_bgcolor='#fff' )

        fig.update_yaxes(range=[hist_min - 10 , hist_max + 10])
        fig.update_xaxes(range=[0, hist_length+pred_length])
    else:
        fig = px.line(data_hist_pred.iloc[0:hist_length+1], x=data_hist_pred.iloc[0:hist_length+1].index,
                            y=symbol,
                            title='Development of a stock price',
                            )
        
        fig.update_layout(plot_bgcolor='#fff' )

        fig.update_yaxes(range=[hist_min - 10 , hist_max + 10])
        fig.update_xaxes(range=[0, hist_length+pred_length])

    fig.update_layout(paper_bgcolor='#fff',
        xaxis_title="Trading Day",
        yaxis_title="Stock price"
        )



    # draw line to mark end of history
    fig.add_shape(type="line",
        xref="x", yref="y",
        x0=hist_length, y0=hist_min - 10, x1=hist_length, y1=hist_max + 10,
        line=dict(
            dash = "dot",
            color="Black",
            width=1,
        ),
    )

       #

    # Calc the implied slope of second model to adjust the fits, draw predictions.

    # TODO: Loop over the elements in shift_points. For empty list, produce neutral graph.





    final_slope = 0.7/20



    if shift_points == []:

        if show_outcome == False:
            fig.write_image("graphs/no_trends/" + symbol + str(start) + " " + str(hist_length) + " " + str(pred_length) + " no model "  + ".png")
        if show_outcome == True:
            fig.write_image("graphs/no_trends/" + symbol + str(start) + " " + str(hist_length) + " " + str(pred_length) + " no model "  + "reveal" + ".png")

    #TODO: Write how to avoid error with single switching point. 

    # if len(shift_points)==1:

    else: 
        for n in range(0,len(shift_points)):
            # TODO: Check again whether this works. 
            #Initialize the shifting points, account for the first and last trend.

            # Draw the first trend until first shifting point.
            if n==0:
                fig.add_shape(type="line",
                    xref="x", yref="y",
                    x0=0, y0=data_hist_pred[symbol].iloc[0], x1=shift_points[0], y1=data_hist_pred[symbol].iloc[shift_points[0]],
                    line=dict(
                        #dash = "dot",
                        color="LightSeaGreen",
                        width=2,
                    ),
                )

            x0 = shift_points[n]
            y0 = data_hist_pred[symbol].iloc[x0]

            # Last trend line goes to the end of the history.
            if n==len(shift_points) - 1:
                x1 = hist_length
            else: 
                x1 = shift_points[n+1]

            y1 = data_hist_pred[symbol].iloc[x1]


            point_1 = data_hist_pred[symbol].iloc[shift_points[n]]

            point_2 = data_hist_pred[symbol].iloc[hist_length]

            slope = 0
            if hist_length != shift_points[n]:
                slope= (y1 - y0) / (x1 - x0)

            # print("Slope of segment {}: ".format(n) + str(slope))

            if n == len(shift_points)-1:
                final_slope = slope 

            fig.add_shape(type="line",
                xref="x", yref="y",
                x0=x0, y0=y0, x1=x1, y1=y1,
                line=dict(
                    #dash = "dot",
                    color="LightSeaGreen",
                    width=2,
                ),
            )

            # fig.add_shape(type="line",
            #     xref="x", yref="y",
            #     x0=shift_points[n], y0=hist_min - 10, x1=shift_points[n], y1=hist_max + 10,
            #     line=dict(
            #         dash = "dot",
            #         color="Black",
            #         width=1,
            #     ),
            # )


    # Add points to note the switching.

    if shift_points !=[]:
        fig.add_traces(
            px.scatter(
                        data_hist_pred.iloc[shift_points], x=data_hist_pred.iloc[shift_points].index,
                        #data_hist_pred.iloc[hist_length: hist_length+1], x=data_hist_pred.iloc[hist_length: hist_length+1].index,
                                y=symbol).update_traces(marker_size=8, marker_color="LightSeaGreen").data
        )


        # Prediction line
        
        point_2 = data_hist_pred[symbol].iloc[hist_length]

        fig.add_shape(type="line",
            xref="x", yref="y",
            x0=hist_length, y0=data_hist_pred[symbol].iloc[hist_length], x1=hist_length + pred_length, y1=point_2 + final_slope * (pred_length),
            line=dict(
                dash = "dot",
                color="LightSeaGreen",
                width=2,
            ),
        )



    fig.write_image("graphs/n_trends/" + symbol + str(start) + " " + str(hist_length) + " " + str(pred_length) + " " + str(len(shift_points)) + " models.png")



    pass
