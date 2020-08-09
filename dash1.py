import numpy as np  
import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 
import dash   
import dash_core_components as dcc   
import dash_html_components as html     

df=pd.read_csv('DashBoard/PM-DATA.csv')
app=dash.Dash()

x_val=df['date']
y_val=df['Beijing']
list_of_city=[col for col in df.columns]
trace0 = go.Scatter(x=df['date'],
                   y=y_val ,
                   mode='lines',
                   name='Beijing'
                    )

trace1 = go.Scatter(x=df['date'],
                y=df['Hong Kong'],
                mode='lines',
                name='Hong Kong'

)     
trace2 = go.Scatter(x=df['date'],
                y=df['Delhi'],
                mode='lines',
                name='Delhi1'

)  
trace3 = go.Scatter(x=df['date'],
                y=df['Los-Angeles'],
                mode='lines',
                name='Los-Angeles'

)  
trace4 = go.Scatter(x=df['date'],
                y=df['New-York'],
                mode='lines',
                name='New-York'

)  
trace5 = go.Scatter(x=df['date'],
                y=df['Paris'],
                mode='lines',
                name='Paris'

)  

trace6 = go.Scatter(x=df['date'],
                y=df['Seoul'],
                mode='lines',
                name='Seoul'

)
trace7 = go.Scatter(x=df['date'],
                y=df['California'],
                mode='lines',
                name='California'

)                 
trace8 = go.Scatter(x=df['date'],
                y=df['Wuhan'],
                mode='lines',
                name='Wuhan'

)
# Now we'll set up the data
data=[trace0,trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8]

app.layout=html.Div(children=[
        html.H1('Air PM level before and after corona'),
        html.Div('Pollution level of different major cities of their country'),
        dcc.Graph(id='pollution',
            figure={'data':data, 'layout':{'title':'Pollution Plots!',
                                        'yaxis':{'title':'PM level of air'},
                                        'plot_bgcolor':'#00203FFF',
                                        'paper_bgcolor':'#ADEFD1FF',
                                        'font':{'color':'black'},
                                        }}
            ),
        html.H3('PM, also known as particle pollution, is a complex mixture of air-borne particles and liquid droplets composed of acids (such as nitrates and sulfates), ammonium, water, black (or "elemental") carbon, organic chemicals, metals, and soil (crustal) material.'),
        html.Img(src=('covidimage.jpg'))
])



if __name__=='__main__':
    app.run_server()