from django.shortcuts import render
import pandas as pd 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import urllib, base64
import io
pd.set_option('display.max_colwidth',60)
import os
import chart_studio.plotly as py
import plotly.offline as pyoff
import plotly.graph_objs as go

# Create your views here.
def home(request):
    a = pd.read_csv('traffic/cv.csv')
    df = pd.read_csv('traffic/overviewcsv.csv')
    plot_data = [
        go.Scatter(
            x=df['DeviceTimeStamp'],
            y=df['OTI'],
            name='OTI'
        ),
        go.Scatter(
            x=df['DeviceTimeStamp'],
            y=df['ATI'],
            name='ATI'
        ),
        go.Scatter(
            x=df['DeviceTimeStamp'],
            y=df['OLI'],
            name='OLI'
        ),
    ]
    plot_layout = go.Layout(
            title='OTI Vs Time',
            yaxis_title = "OTI",
            xaxis_title = "Time",
        )
    fig = go.Figure(data=plot_data, layout=plot_layout)
    # pyoff.iplot(fig)
    graph_div = pyoff.plot(fig, auto_open = False, output_type="div")



    
    # original1 = pd.read_csv('traffic/cv.csv')
    # plot_data = [
    #     go.Scatter(
    #         x=original1.index,
    #         y=original1['IL2'],
    #         name='IL2'
    #     ),
    #     go.Scatter(
    #         x=prd.index,
    #         y=prd[0],
    #         name='Predicted'
    #     ),
    #     go.Scatter(
    #         x=ub.index,
    #         y=ub[0],
    #         name='Upper Bound'
    #     ),
    #     go.Scatter(
    #         x=trn.index,
    #         y=trn[0],
    #         name='Training'
    #     ),
    #     go.Scatter(
    #         x=lb.index,
    #         y=lb[0],
    #         name='Lower Bound'
    #     )
    
    
    # ]
    # plot_layout = go.Layout(
    #         title='Load, rmse='+str(rmse)
    #     )
    # fig1 = go.Figure(data=plot_data, layout=plot_layout)
    # graph_div_ = pyoff.plot(fig1, auto_open = False, output_type="div")
    
    

    return render(request,'traffic/graphh.html',{'graph_div':graph_div})
                                   
