import os
import plotly.graph_objs as go
import plotly.offline as py
from plotly import tools

def visualize(rawdata, rawdata2, main_title, x_title, y_title, x2_title, y2_title):

    #Initialize the Data
    trace=go.Bar(
        {
            'x': rawdata[x_title],
            'y': rawdata[y_title],
        },
    )
    trace2=go.Bar(
        {
            'x': rawdata2[x2_title],
            'y': rawdata2[y2_title],
        },
        xaxis='x2',
        yaxis='y2',
    )
    data=[trace, trace2]

    #Initialize Layouts
    layout_style=go.Layout(
        title=main_title,
        xaxis=dict(
            domain=[0, 0.45],
            title=x_title,
            zeroline=True,
            showline=True,
            autotick=True,
            ticks='outside',
            ticklen=8,
            tickwidth=4,
            tickcolor='#000',
            autorange=True,
            linewidth=6
        ),
        yaxis=dict(
            title=y_title,
            zeroline=True,
            showline=True,
            autotick=True,
            ticks='outside',
            ticklen=8,
            tickwidth=4,
            tickcolor='#000',
            linewidth=6
        ),
        xaxis2=dict(
            domain=[0.55, 1],
            title=x2_title,
            zeroline=True,
            showline=True,
            autotick=True,
            ticks='outside',
            ticklen=8,
            tickwidth=4,
            tickcolor='#000',
            autorange=True,
            linewidth=6
        ),
        yaxis2=dict(
            title=y2_title,
            zeroline=True,
            showline=True,
            autotick=True,
            ticks='outside',
            ticklen=8,
            tickwidth=4,
            tickcolor='#000',
            linewidth=6,
            anchor='x2',
        ),
        font=dict(
            family='Times New Roman, Times, Serif',
        ),
        showlegend=False,
    )

    #For saving the graph into the desktop folder
    dir_output=os.path.join(
        '~',
        'Desktop',
        'absconbest_payroll',
        'output'
    )
    dir_output=os.path.expanduser(dir_output)

    #Follow Plotly API's standards
    fig = go.Figure(data=data, layout=layout_style)
    py.plot(
        fig,
        auto_open=True,
        filename=os.path.join(
            dir_output,
            main_title.lower().replace(" ","_").replace(",","")+'.html'
        ),
        image_filename=os.path.join(
            dir_output,
            main_title.lower().replace(" ","_").replace(",","")
        )
    )
