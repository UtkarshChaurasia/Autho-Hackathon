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


# Traces for pollution level in 2020 only
traceD=go.Scatter(x=df['date'].iloc[0:112],
                y=df['Delhi'],
                mode='lines+markers',
                name='Delhi-2020'
)
traceB = go.Scatter(x=df['date'].iloc[0:112],
                   y=y_val ,
                   mode='lines+markers',
                   name='Beijing-2020'
                    )
traceH = go.Scatter(x=df['date'].iloc[0:112],
                y=df['Hong Kong'],
                mode='lines+markers',
                name='Hong Kong-2020'
) 
traceL = go.Scatter(x=df['date'].iloc[0:112],
                y=df['Los-Angeles'],
                mode='lines+markers',
                name='Los-Angeles-2020'

) 
traceN = go.Scatter(x=df['date'].iloc[0:112],
                y=df['New-York'],
                mode='lines+markers',
                name='New-York-2020'

)  
traceP = go.Scatter(x=df['date'].iloc[0:112],
                y=df['Paris'],
                mode='lines+markers',
                name='Paris-2020'

)  
traceS = go.Scatter(x=df['date'].iloc[0:112],
                y=df['Seoul'],
                mode='lines+markers',
                name='Seoul-2020'

)
traceC = go.Scatter(x=df['date'].iloc[0:112],
                y=df['California'],
                mode='lines+markers',
                name='California-2020'

)
traceW = go.Bar(x=df['date'].iloc[0:112],
                y=df['Wuhan'],
                name='Wuhan-2020'

)
traceNY=go.Bar(x=df['date'].iloc[0:112],
            y=df['New-York'],
            name='New-York-2020',

)
tracecb=go.Bar(x=df['date'].iloc[0:112],
            y=df['California'],
            name='California-2020',

)
tracepb=go.Bar(x=df['date'].iloc[0:112],
            y=df['Paris'],
            name='Paris-2020',

)
tracedb=go.Bar(x=df['date'].iloc[0:112],
            y=df['Delhi'],
            name='Delhi-2020',

)
tracehb=go.Bar(x=df['date'].iloc[0:112],
            y=df['Hong Kong'],
            name='Hong-Kong-2020',

)
tracesb=go.Bar(x=df['date'].iloc[0:112],
            y=df['Seoul'],
            name='Seoul-2020',

)
tracebb=go.Bar(x=df['date'].iloc[0:112],
            y=df['Beijing'],
            name='Beijing-2020',

)
tracelb=go.Bar(x=df['date'].iloc[0:112],
            y=df['Los-Angeles'],
            name='Los-Angeles-2020',

)

dataDB=[traceD,traceB]
dataHL=[traceH,traceL]
dataNP=[traceN,traceP]
dataSC=[traceS,traceC]
data2020=[traceW,traceNY,tracecb,tracepb,tracedb,tracehb,tracesb,tracebb,tracelb]
# Now we create the app layout

app.layout=html.Div(children=[
        html.H1(['VISUALIZATION OF AIR PM LEVEL BEFORE AND AFTER COVID-19'],style={'textAlign':'center',
                                                                'backgroundColor':'#000000',
                                                                'color':'#FFFFFF',
                                                                'display':'inline_block',
                                                                'border-radius': '30px',
                                                                'padding': '10px 10px 10px 10px',
                                                                'font-size': '60px',
                                                                'font-family': 'Impact, Haettenschweiler, Arial Narrow Bold, sans-serif',
                                                                }),
        html.H2(['Pollution level of major cities around the globe'],style={
                                                                    'textAlign':'center',
                                                                    'font-family': 'Impact, Haettenschweiler, Arial Narrow Bold, sans-serif',
                                                                    'font-weight': '600',
                                                                    'font-size': '30px',
                                                                }),
        html.H3(['PM, also known as particle pollution, is a complex mixture of air-borne particles and liquid droplets composed of acids (such as nitrates and sulfates), ammonium, water, black (or "elemental") carbon, organic chemicals, metals, and soil (crustal) material.'],
                                                                style={
                                                                    'font-family': 'Impact, Haettenschweiler, Arial Narrow Bold, sans-serif',
                                                                    'font-weight': 'inherit',
                                                                    'padding': '0px 100px 15px 100px',
                                                                }),
        dcc.Graph(id='pollution',
            figure={'data':data, 'layout':{'title':'Pollution Plots!',
                                        'yaxis':{'title':'PM level of air'},
                                        'plot_bgcolor':'#00203FFF',
                                        'paper_bgcolor':'#ADEFD1FF',
                                        'font':{'color':'black'},
                                        }}
            ),
            
        dcc.Graph(id='pollution2',
            figure={'data':dataDB, 'layout':{'title':'Pollution Plots Delhi and Beijing in 2020',
                                        'yaxis':{'title':'PM level of air'},
                                        'plot_bgcolor':'#F1F3FFFF',
                                        'paper_bgcolor':'#FC766AFF',
                                        'font':{'color':'black'},
                                        }}
            ),
            
        dcc.Graph(id='pollution3',
            figure={'data':dataHL, 'layout':{'title':'Pollution Plots Hong-Kong and Los-Angeles in 2020',
                                        'yaxis':{'title':'PM level of air'},
                                        'plot_bgcolor':'#00203FFF',
                                        'paper_bgcolor':'#ADEFD1FF',
                                        'font':{'color':'black'},
                                        }}
            ),
        dcc.Graph(id='pollution4',
            figure={'data':dataNP, 'layout':{'title':'Pollution Plots New-York and Paris in 2020',
                                        'yaxis':{'title':'PM level of air'},
                                        'plot_bgcolor':'#F1F3FFFF',
                                        'paper_bgcolor':'#FC766AFF',
                                        'font':{'color':'black'},
                                        }}
            ),
        dcc.Graph(id='pollution5',
            figure={'data':dataSC, 'layout':{'title':'Pollution Plots Seoul and California in 2020',
                                        'yaxis':{'title':'PM level of air'},
                                        'plot_bgcolor':'#00203FFF',
                                        'paper_bgcolor':'#ADEFD1FF',
                                        'font':{'color':'black'},
                                        }}
            ),
        dcc.Graph(id='pollution6',
            figure={'data':data2020, 'layout':{'title':'Pollution Plots of different cities to compare them all!',
                                        'yaxis':{'title':'PM level of air'},
                                        'plot_bgcolor':'#F1F3FFFF',
                                        'paper_bgcolor':'#FC766AFF',
                                        'font':{'color':'black'},
                                        'barmode':'stack'
                                        }}
            )
        
        
])



if __name__=='__main__':
    app.run_server()
