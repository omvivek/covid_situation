from pywebio.input import * #input, FLOAT,input_group,textarea,radio,select,DATE
from pywebio.output import *  #put_text,put_warning,put_success,put_info,toast,popup,put_image,put_markdown,OutputPosition,put_processbar,set_processbar,clear
import urllib
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import re
import time
import pandas_datareader as web
import datetime as dt
import mplfinance as mpf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense,Dropout,LSTM
from tensorflow.keras.models import Sequential
from pywebio.input import *
from pywebio.output import *
from pywebio import input as pin
from pywebio import output as pout
import plotly.graph_objects as go

#https://graphics.reuters.com/world-coronavirus-tracker-and-maps/countries-and-territories/india/
def covid_app():
    import pandas as pd
    #put_processbar('bar')
    #for i in range(1, 11):
        #set_processbar('bar', i / 10)
    from pygame import mixer
    mixer.init()
    mixer.music.load("wait.mp3")
    mixer.music.play()
    put_text("Please Wait While Loading The Data .......")
    df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
    country = df['Country'].unique()
    #time.sleep(2)
    #toast("Loading The Data .......")
    from pygame import mixer
    mixer.init()
    mixer.music.load("country.mp3")
    mixer.music.play()
    user_info=select("Choose The Country",country)#radio
    if user_info not in country:
        put_warning('Sorry ,once check the country name. Example : India')
    else:
        put_success("Congrats, You Can Go Further With The Detail's Of "+user_info)
        date = df["Date_reported"].unique()
        #start =input("Start Date：(EX : 2021-09-01)")
        from pygame import mixer
        mixer.init()
        mixer.music.load("date.mp3")
        mixer.music.play()
        start = select("Start Date：",date)
        put_info('Start Date: ',start)
        #end = input("End Date：(EX : 2021-09-30)")
        from pygame import mixer
        mixer.init()
        mixer.music.load("date1.mp3")
        mixer.music.play()
        end = select("End Date：",date)
        put_info('End Date: ',end)
        df_c = df[df.Country == user_info ]
        sep_c =  df_c.loc[(df_c["Date_reported"] >= start) & (df_c["Date_reported"] <= end)]
        x = sep_c["Date_reported"]
        y = sep_c["New_cases"]
        z = sep_c["New_deaths"]
        from pygame import mixer
        mixer.init()
        mixer.music.load("graph.mp3")
        mixer.music.play()
        graphtype=select("Choose The Type Of Graph",options=['Bar','Line','Pie','Scatter','On map','Table'])#radio
        #put_text(graphtype)
        #start of the bar graph
        if graphtype == 'Bar':
            from pygame import mixer
            mixer.init()
            mixer.music.load("bar.mp3")
            mixer.music.play()
            put_markdown('## Bar Graph')
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose :",["day's VS new_cases's and death's","day's VS new_case's","day's VS new_death's","end"]) 
                if tybar == "day's VS new_cases's and death's":
                    put_markdown("## day's VS new_cases's and death's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cd.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=x,y=y,name='New_cases',marker_color='indianred'))
                    fig.add_trace(go.Bar(x=x,y=z,name='New_deaths',marker_color='lightsalmon'))
                    fig.update_layout(title=user_info+"'s Covid Situation From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='cases count',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
#https://pywebio.readthedocs.io/en/latest/
#https://pywebio-charts.pywebio.online/?app=plotly
                elif tybar == "day's VS new_case's":
                    put_markdown("## day's VS new_case's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cdd.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('indianred')
        #df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                    fig = px.bar(x=x,y=y,color_discrete_sequence=col)
                    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                    fig.update_layout(title=user_info+"'s Cases From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='cases',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS new_death's":
                    put_markdown("## day's VS new_death's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cdde.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        #df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                    fig = px.bar(x=x,y=z,color_discrete_sequence=col)
                    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                    fig.update_layout(title=user_info+"'s Deaths From "+start+" To "+end,
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='deaths',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
        elif graphtype == 'Line':
            from pygame import mixer
            mixer.init()
            mixer.music.load("line.mp3")
            mixer.music.play()
            put_markdown('## Line Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS new_cases's and death's","day's VS new_case's","day's VS new_death's","end"])
                if tybar == "day's VS new_cases's and death's":
                    put_markdown("## day's VS new_cases's and death's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cd.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    import plotly.graph_objects as go
        #df = px.data.gapminder().query("continent=='Oceania'")
        #fig = px.line(df,x=y, y=z,color_discrete_sequence=col )
                    fig = go.Figure()
                    fig.add_trace(go.Line(x=x,y=y,name='New_cases',marker_color='indianred'))
                    fig.add_trace(go.Line(x=x,y=z,name='New_deaths',marker_color='lightsalmon'))
                    fig.update_layout(title=user_info+"'s Covid Situation From "+start+" To "+end,
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='cases count',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(x=0,y=1.0,bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS new_case's":
                    put_markdown("## day's VS new_case's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cdd.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('indianred')
        #df = px.data.gapminder().query("continent=='Oceania'")
                    fig = px.line(x=x, y=y,color_discrete_sequence=col )
                    fig.update_layout(title=user_info+"'s Cases From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='cases',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS new_death's":
                    put_markdown("## day's VS new_death's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cdde.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        #df = px.data.gapminder().query("continent=='Oceania'")
                    fig = px.line(x=x, y=z,color_discrete_sequence=col )
                    fig.update_layout(title=user_info+"'s Deaths From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='deaths',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == 'end':
                    i=1
        elif graphtype == 'Pie':
            from pygame import mixer
            mixer.init()
            mixer.music.load("pie.mp3")
            mixer.music.play()
            put_markdown('## Pie Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS new_cases's and death's","day's VS new_case's","day's VS new_death's","end"])
                if tybar == "day's VS new_cases's and death's":
                    put_markdown("## day's VS new_cases's and death's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cd.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    from plotly.subplots import make_subplots
                    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
                    fig.add_trace(go.Pie(labels=x, values=y, name="case's"),1, 1)
                    fig.add_trace(go.Pie(labels=x, values=z, name="death's"),1, 2)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title_text=user_info+"'s Covid Situation From "+start+" To "+end)
            
        # Add annotations in the center of the donut pies.
            
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS new_case's":
                    put_markdown("## day's VS new_case's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cdd.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
        #df = px.data.gapminder().query("continent == 'Asia'")
                    fig = px.pie(values=y, names=x)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title=user_info+"'s Cases From "+start+" To "+end)
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS new_death's":
                    put_markdown("## day's VS new_death's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cdde.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
        #df = px.data.gapminder().query("continent == 'Asia'")
                    fig = px.pie(values=z, names=x)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title=user_info+"'s Deaths From "+start+" To "+end)
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
            
        elif graphtype == 'Scatter':
            from pygame import mixer
            mixer.init()
            mixer.music.load("scatter.mp3")
            mixer.music.play()
            put_markdown('## Scatter Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS new_cases's and death's","day's VS new_case's","day's VS new_death's","end"])
                if tybar == "day's VS new_cases's and death's":
                    put_markdown("## day's VS new_cases's and death's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cd.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=y,y=x,name='Cases',
                    marker=dict(
                    color='rgba(156, 165, 196, 0.95)',
                    line_color='rgba(156, 165, 196, 1.0)',
                    )
                    ))
                    fig.add_trace(go.Scatter(x=z, y=x,name='Deaths',
                    marker=dict(
                    color='rgba(204, 204, 204, 0.95)',
                    line_color='rgba(217, 217, 217, 1.0)'
                    )
                    ))

                    fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=10))
    
                    fig.update_layout(
                    title=user_info+"'s Covid Situation From "+start+" To "+end,
                    margin=dict(l=140, r=40, b=50, t=80),
                    legend=dict(
                    font_size=10,
                    yanchor='middle',
                    xanchor='right',
                    ),
                    width=800,
                    height=600,
                    paper_bgcolor='white',
                    plot_bgcolor='white',
                    hovermode='closest',
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS new_case's":
                    put_markdown("## day's VS new_case's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cdd.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    import pandas as pd
        #df = pd.DataFrame(dict(school=x, salary=y,gender=x))
                    col=[]
                    for i in x:
                        col.append('indianred')
        # Use column names of df for the different parameters x, y, color, ...
                    fig = px.scatter(x=x, y=y,color_discrete_sequence=col,
                     title=user_info+"'s Cases From "+start+" To "+end,
                     labels={"x":"day's","y":"case's"} # customize axis label
                    )

                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS new_death's":
                    put_markdown("## day's VS new_death's")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cdde.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    import pandas as pd
        #df = pd.DataFrame(dict(school=x, salary=y,gender=x))
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        # Use column names of df for the different parameters x, y, color, ...
                    fig = px.scatter(x=x, y=z,color_discrete_sequence=col,
                     title=user_info+"'s Deaths From "+start+" To "+end)
                    fig.update_layout(title=user_info+"'s Deaths From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='deaths',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )

                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
        elif graphtype == 'On map':
            from pygame import mixer
            mixer.init()
            mixer.music.load("onmap.mp3")
            mixer.music.play()
            put_markdown('## On Map')
            time.sleep(2)
            from pygame import mixer
            mixer.init()
            mixer.music.load("wait.mp3")
            mixer.music.play()
            put_text("Please Wait While Loading The Data .......")
            from pywebio.output import put_html
            import plotly.express as px
            import pandas as pd
            df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
            df_c = df[df.Country == user_info]
            sep_c =  df_c.loc[(df_c["Date_reported"] >= start) & (df_c["Date_reported"] <= end)]
            x = sep_c["Date_reported"]
            y = sep_c["New_cases"]
            country=sep_c["Country"]
            
            df1 = px.data.gapminder()
            Country=df1['country'].unique()
            from pygame import mixer
            mixer.init()
            mixer.music.load("country.mp3")
            mixer.music.play()
            user_info1=select("Choose The Country",Country)
            df1=df1[['country', 'iso_alpha']]
            try:
                df1=df1[df1.country == user_info1]
                df1=df1.reset_index()
                idd=df1["iso_alpha"][0]
                loc=[]
                for i in x:
                    loc.append(idd)
                fig = px.scatter_geo(sep_c,locations=loc, color=x,
                     hover_name=country,hover_data=['New_cases','New_deaths'],
                     projection="natural earth",
                     animation_frame=x,title=user_info+"'s Covid Situation From "+start+" To "+end)
                
                html = fig.to_html(include_plotlyjs="require", full_html=False)
                put_html(html)
                fig = px.scatter_geo(sep_c,locations=loc, color=x,
                     hover_name=country,hover_data=['New_cases','New_deaths'],
                     projection="orthographic",
                     animation_frame=x,title=user_info+"'s Covid Situation From "+start+" To "+end)
                html = fig.to_html(include_plotlyjs="require", full_html=False)
                put_html(html)
            except:
                toast("Something Went Wrong",color='red')
                

# Use column names of df for the different parameters x, y, color, ...
            
            

        elif graphtype == 'Table':
            from pygame import mixer
            mixer.init()
            mixer.music.load("table.mp3")
            mixer.music.play()
            put_markdown('## Table')
            time.sleep(2)
            from pywebio.output import put_html
            import plotly.graph_objects as go
            from plotly.colors import n_colors
            import numpy as np
            np.random.seed(1)

            colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
            a = x
            b = y
            c = z
            headerColor = 'grey'
            col=[]
            for i in x:
                col.append('white')
            fig = go.Figure(data=[go.Table(
            header=dict(
            values=['<b>days</b>', '<b>cases</b>', '<b>deaths</b>'],
            line_color='darkslategray',fill_color='white',
            align='center',font=dict(color='black', size=12)
            ),
            cells=dict(
            values=[a, b, c],
            line_color='darkslategray',
            fill_color =col,
            align='center', font=dict(color='black', size=11)
            ))
            ])

            html = fig.to_html(include_plotlyjs="require", full_html=False)
            put_html(html)

def india_app():
    df = pd.read_csv('covid_19_india.csv')
    #df=df.replace(to_replace ="-",value ="0")
    df['Date']=pd.to_datetime(df.Date)
    state=df["State"].unique()
    from pygame import mixer
    mixer.init()
    mixer.music.load("state.mp3")
    mixer.music.play()
    state=select("Choose The State : ",state)
    put_success("Congrats, You Can Go Further With The Detail's Of "+state)
    time.sleep(3)
    from pygame import mixer
    mixer.init()
    mixer.music.load("choose.mp3")
    mixer.music.play()
    confirmed=select("Choose : ",["Cured vs Deaths","Cured vs Confirmed","Deaths vs Confirmed"])
    #put_text(state)
    from pygame import mixer
    mixer.init()
    mixer.music.load("date.mp3")
    mixer.music.play()
    start = input("Start Date：",type=DATE)
    put_info('Start Date: ',start)
#put_text(date)
#start=input("From : ",type=DATE)
#put_text(start)
    from pygame import mixer
    mixer.init()
    mixer.music.load("date1.mp3")
    mixer.music.play()
    end = input("End Date：",type=DATE)
    put_info('End Date: ',end)
#end=input("End : ",type=DATE)
#put_text(end)
    df_c=df[df.State == state]
    sep_c =  df_c.loc[(df_c["Date"] >= start) & (df_c["Date"] <= end)]
    x = sep_c["Date"]
    if confirmed == "Cured vs Deaths":
        y = sep_c["Cured"]
        z = sep_c["Deaths"]
        from pygame import mixer
        mixer.init()
        mixer.music.load("graph.mp3")
        mixer.music.play()
        graphtype=select("Choose The Type Of Graph",options=['Bar','Line','Pie','Scatter','Table'])#radio
        if graphtype == 'Bar':
            from pygame import mixer
            mixer.init()
            mixer.music.load("bar.mp3")
            mixer.music.play()
            put_markdown('## Bar Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose :",["day's VS Cured and Deaths","day's VS Cured","day's VS Deaths","end"])
                if tybar == "day's VS Cured and Deaths":
                    put_markdown("## day's VS Cured and Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cur.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=x,y=y,name="Cured",marker_color='indianred'))
                    fig.add_trace(go.Bar(x=x,y=z,name="Deaths",marker_color='lightsalmon'))
                    fig.update_layout(title=state+"'s Cured and Death's From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Cured and Death's",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
#https://pywebio.readthedocs.io/en/latest/
#https://pywebio-charts.pywebio.online/?app=plotly
                elif tybar == "day's VS Cured":
                    put_markdown("## day's VS Cured")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cured.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('indianred')
        #df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                    fig = px.bar(x=x,y=y,color_discrete_sequence=col)
                    fig.update_traces(textposition='outside')
                    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Cured From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Cured",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Deaths":
                    put_markdown("## day's VS Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("death.mp3")
                    mixer.music.play()
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        #df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                    fig = px.bar(x=x,y=z,color_discrete_sequence=col)
                    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Death's From "+start+" To "+end,
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Deaths",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
        elif graphtype == 'Line':
            from pygame import mixer
            mixer.init()
            mixer.music.load("line.mp3")
            mixer.music.play()
            put_markdown('## Line Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Cured and Deaths","day's VS Cured","day's VS Deaths","end"])
                if tybar == "day's VS Cured and Deaths":
                    put_markdown("## day's VS Cured and Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cur.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    import plotly.graph_objects as go
        #df = px.data.gapminder().query("continent=='Oceania'")
        #fig = px.line(df,x=y, y=z,color_discrete_sequence=col )
                    fig = go.Figure()
                    fig.add_trace(go.Line(x=x,y=y,name='Cured',marker_color='indianred'))
                    fig.add_trace(go.Line(x=x,y=z,name='Deaths',marker_color='lightsalmon'))
                    fig.update_layout(title=state+"'s Cured and Deaths From "+start+" To "+end,
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Cured and Deaths',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(x=0,y=1.0,bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Cured":
                    put_markdown("## day's VS Cured")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cured.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('indianred')
        #df = px.data.gapminder().query("continent=='Oceania'")
                    fig = px.line(x=x, y=y,color_discrete_sequence=col )
                    fig.update_layout(title=state+"'s Cured From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Cured',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Deaths":
                    put_markdown("## day's VS Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("death.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        #df = px.data.gapminder().query("continent=='Oceania'")
                    fig = px.line(x=x, y=z,color_discrete_sequence=col )
                    fig.update_layout(title=state+"'s Deaths From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Deaths',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == 'end':
                    i=1
        elif graphtype == 'Pie':
            from pygame import mixer
            mixer.init()
            mixer.music.load("pie.mp3")
            mixer.music.play()
            put_markdown('## Pie Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Cured and Deaths","day's VS Cured","day's VS Deaths","end"])
                if tybar == "day's VS Cured and Deaths":
                    put_markdown("## day's VS Cured and Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cur.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    from plotly.subplots import make_subplots
                    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
                    fig.add_trace(go.Pie(labels=x, values=y, name="Cured"),1, 1)
                    fig.add_trace(go.Pie(labels=x, values=z, name="Deaths"),1, 2)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title_text=state+"'s Cured and Deaths From "+start+" To "+end)
            
        # Add annotations in the center of the donut pies.
            
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Cured":
                    put_markdown("## day's VS Cured")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cured.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
        #df = px.data.gapminder().query("continent == 'Asia'")
                    fig = px.pie(values=y, names=x)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Cured From "+start+" To "+end)
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Deaths":
                    put_markdown("## day's VS Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("death.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
        #df = px.data.gapminder().query("continent == 'Asia'")
                    fig = px.pie(values=z, names=x)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Deaths From "+start+" To "+end)
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
            
        elif graphtype == 'Scatter':
            from pygame import mixer
            mixer.init()
            mixer.music.load("scatter.mp3")
            mixer.music.play()
            put_markdown('## Scatter Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Cured and Deaths","day's VS Cured","day's VS Deaths","end"])
                if tybar == "day's VS Cured and Deaths":
                    put_markdown("## day's VS Cured and Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cur.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=y,y=x,name='Cured',
                    marker=dict(
                    color='rgba(156, 165, 196, 0.95)',
                    line_color='rgba(156, 165, 196, 1.0)',
                    )
                    ))
                    fig.add_trace(go.Scatter(x=z, y=x,name='Deaths',
                    marker=dict(
                    color='rgba(204, 204, 204, 0.95)',
                    line_color='rgba(217, 217, 217, 1.0)'
                    )
                    ))

                    fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=10))
    
                    fig.update_layout(
                    title=state+"'s Cured and Deaths From "+start+" To "+end,
                    margin=dict(l=140, r=40, b=50, t=80),
                    legend=dict(
                    font_size=10,
                    yanchor='middle',
                    xanchor='right',
                    ),
                    width=800,
                    height=600,
                    paper_bgcolor='white',
                    plot_bgcolor='white',
                    hovermode='closest',
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Cured":
                    put_markdown("## day's VS Cured")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cured.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px

        #df = pd.DataFrame(dict(school=x, salary=y,gender=x))
                    col=[]
                    for i in x:
                        col.append('indianred')
        # Use column names of df for the different parameters x, y, color, ...
                    fig = px.scatter(x=x, y=y,color_discrete_sequence=col,
                     title=state+"'s Cured From "+start+" To "+end,
                     labels={"x":"day's","y":"Cured"} # customize axis label
                    )

                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Deaths":
                    put_markdown("## day's VS Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("death.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    
        #df = pd.DataFrame(dict(school=x, salary=y,gender=x))
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        # Use column names of df for the different parameters x, y, color, ...
                    fig = px.scatter(x=x, y=z,color_discrete_sequence=col,
                     title=state+"'s Deaths From "+start+" To "+end)
                    fig.update_layout(title=state+"'s Deaths From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='deaths',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )

                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1

# Use column names of df for the different parameters x, y, color, ...
            
            

        elif graphtype == 'Table':
            from pygame import mixer
            mixer.init()
            mixer.music.load("table.mp3")
            mixer.music.play()
            put_markdown('## Table')
            time.sleep(2)
            from pywebio.output import put_html
            import plotly.graph_objects as go
            from plotly.colors import n_colors
            np.random.seed(1)

            colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
            a = x
            b = y
            c = z
            headerColor = 'grey'
            col=[]
            for i in x:
                col.append('white')
            fig = go.Figure(data=[go.Table(
            header=dict(
            values=['<b>days</b>', '<b>Cured</b>', '<b>deaths</b>'],
            line_color='darkslategray',fill_color='white',
            align='center',font=dict(color='black', size=12)
            ),
            cells=dict(
            values=[a, b, c],
            line_color='darkslategray',
            fill_color =col,
            align='center', font=dict(color='black', size=11)
            ))
            ])

            html = fig.to_html(include_plotlyjs="require", full_html=False)
            put_html(html)
                    
    elif confirmed == "Cured vs Confirmed":
        y = sep_c["Cured"]
        z = sep_c["Confirmed"]
        from pygame import mixer
        mixer.init()
        mixer.music.load("graph.mp3")
        mixer.music.play()
        graphtype=select("Choose The Type Of Graph",options=['Bar','Line','Pie','Scatter','Table'])#radio
        if graphtype == 'Bar':
            from pygame import mixer
            mixer.init()
            mixer.music.load("bar.mp3")
            mixer.music.play()
            put_markdown('## Bar Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose :",["day's VS Cured and Confirmed","day's VS Cured","day's VS Confirmed","end"])
                if tybar == "day's VS Cured and Confirmed":
                    put_markdown("## day's VS Cured and Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cuco.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=x,y=y,name="Cured",marker_color='indianred'))
                    fig.add_trace(go.Bar(x=x,y=z,name="Confirmed",marker_color='lightsalmon'))
                    fig.update_layout(title=state+"'s Cured and Confirmed From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Cured and Confirmed",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
#https://pywebio.readthedocs.io/en/latest/
#https://pywebio-charts.pywebio.online/?app=plotly
                elif tybar == "day's VS Cured":
                    put_markdown("## day's VS Cured")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cured.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('indianred')
        #df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                    fig = px.bar(x=x,y=y,color_discrete_sequence=col)
                    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Cured From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Cured",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Confirmed":
                    put_markdown("## day's VS Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("con.mp3")
                    mixer.music.play()
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        #df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                    fig = px.bar(x=x,y=z,color_discrete_sequence=col)
                    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Confirmed From "+start+" To "+end,
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Confirmed",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
        elif graphtype == 'Line':
            from pygame import mixer
            mixer.init()
            mixer.music.load("line.mp3")
            mixer.music.play()
            put_markdown('## Line Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Cured and Confirmed","day's VS Cured","day's VS Confirmed","end"])
                if tybar == "day's VS Cured and Confirmed":
                    put_markdown("## day's VS Cured and Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cuco.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    import plotly.graph_objects as go
        #df = px.data.gapminder().query("continent=='Oceania'")
        #fig = px.line(df,x=y, y=z,color_discrete_sequence=col )
                    fig = go.Figure()
                    fig.add_trace(go.Line(x=x,y=y,name='Cured',marker_color='indianred'))
                    fig.add_trace(go.Line(x=x,y=z,name='Confirmed',marker_color='lightsalmon'))
                    fig.update_layout(title=state+"'s Cured and Confirmed From "+start+" To "+end,
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Cured and Confirmed',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(x=0,y=1.0,bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Cured":
                    put_markdown("## day's VS Cured")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cured.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('indianred')
        #df = px.data.gapminder().query("continent=='Oceania'")
                    fig = px.line(x=x, y=y,color_discrete_sequence=col )
                    fig.update_layout(title=state+"'s Cured From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Cured',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Confirmed":
                    put_markdown("## day's VS Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("con.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        #df = px.data.gapminder().query("continent=='Oceania'")
                    fig = px.line(x=x, y=z,color_discrete_sequence=col )
                    fig.update_layout(title=state+"'s Confirmed From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Confirmed',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == 'end':
                    i=1
        elif graphtype == 'Pie':
            from pygame import mixer
            mixer.init()
            mixer.music.load("pie.mp3")
            mixer.music.play()
            put_markdown('## Pie Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Cured and Confirmed","day's VS Cured","day's VS Confirmed","end"])
                if tybar == "day's VS Cured and Confirmed":
                    put_markdown("## day's VS Cured and Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cuco.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    from plotly.subplots import make_subplots
                    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
                    fig.add_trace(go.Pie(labels=x, values=y, name="Cured"),1, 1)
                    fig.add_trace(go.Pie(labels=x, values=z, name="Confirmed"),1, 2)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title_text=state+"'s Cured and Confirmed From "+start+" To "+end)
            
        # Add annotations in the center of the donut pies.
            
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Cured":
                    put_markdown("## day's VS Cured")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cured.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
        #df = px.data.gapminder().query("continent == 'Asia'")
                    fig = px.pie(values=y, names=x)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Cured From "+start+" To "+end)
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Confirmed":
                    put_markdown("## day's VS Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("con.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
        #df = px.data.gapminder().query("continent == 'Asia'")
                    fig = px.pie(values=z, names=x)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Confirmed From "+start+" To "+end)
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
            
        elif graphtype == 'Scatter':
            from pygame import mixer
            mixer.init()
            mixer.music.load("scatter.mp3")
            mixer.music.play()
            put_markdown('## Scatter Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Cured and Confirmed","day's VS Cured","day's VS Confirmed","end"])
                if tybar == "day's VS Cured and Confirmed":
                    put_markdown("## day's VS Cured and Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cuco.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=y,y=x,name='Cured',
                    marker=dict(
                    color='rgba(156, 165, 196, 0.95)',
                    line_color='rgba(156, 165, 196, 1.0)',
                    )
                    ))
                    fig.add_trace(go.Scatter(x=z, y=x,name='Confirmed',
                    marker=dict(
                    color='rgba(204, 204, 204, 0.95)',
                    line_color='rgba(217, 217, 217, 1.0)'
                    )
                    ))

                    fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=10))
    
                    fig.update_layout(
                    title=state+"'s Cured and Confirmed From "+start+" To "+end,
                    margin=dict(l=140, r=40, b=50, t=80),
                    legend=dict(
                    font_size=10,
                    yanchor='middle',
                    xanchor='right',
                    ),
                    width=800,
                    height=600,
                    paper_bgcolor='white',
                    plot_bgcolor='white',
                    hovermode='closest',
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Cured":
                    put_markdown("## day's VS Cured")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("cured.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px

        #df = pd.DataFrame(dict(school=x, salary=y,gender=x))
                    col=[]
                    for i in x:
                        col.append('indianred')
        # Use column names of df for the different parameters x, y, color, ...
                    fig = px.scatter(x=x, y=y,color_discrete_sequence=col,
                     title=state+"'s Cured From "+start+" To "+end,
                     labels={"x":"day's","y":"Cured"} # customize axis label
                    )

                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Confirmed":
                    put_markdown("## day's VS Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("con.mp3")
                    from pywebio.output import put_html
                    import plotly.express as px
                    
        #df = pd.DataFrame(dict(school=x, salary=y,gender=x))
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        # Use column names of df for the different parameters x, y, color, ...
                    fig = px.scatter(x=x, y=z,color_discrete_sequence=col,
                     title=state+"'s Deaths From "+start+" To "+end)
                    fig.update_layout(title=state+"'s Confirmed From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Confirmed',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )

                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1

# Use column names of df for the different parameters x, y, color, ...
            
            

        elif graphtype == 'Table':
            from pygame import mixer
            mixer.init()
            mixer.music.load("table.mp3")
            mixer.music.play()
            put_markdown('## Table')
            time.sleep(2)
            from pywebio.output import put_html
            import plotly.graph_objects as go
            from plotly.colors import n_colors
            np.random.seed(1)

            colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
            a = x
            b = y
            c = z
            headerColor = 'grey'
            col=[]
            for i in x:
                col.append('white')
            fig = go.Figure(data=[go.Table(
            header=dict(
            values=['<b>days</b>', '<b>Cured</b>', '<b>Confirmed</b>'],
            line_color='darkslategray',fill_color='white',
            align='center',font=dict(color='black', size=12)
            ),
            cells=dict(
            values=[a, b, c],
            line_color='darkslategray',
            fill_color =col,
            align='center', font=dict(color='black', size=11)
            ))
            ])

            html = fig.to_html(include_plotlyjs="require", full_html=False)
            put_html(html)
    elif confirmed == "Deaths vs Confirmed":
        y = sep_c["Deaths"]
        z = sep_c["Confirmed"]
        from pygame import mixer
        mixer.init()
        mixer.music.load("graph.mp3")
        mixer.music.play()
        graphtype=select("Choose The Type Of Graph",options=['Bar','Line','Pie','Scatter','Table'])#radio
        if graphtype == 'Bar':
            from pygame import mixer
            mixer.init()
            mixer.music.load("bar.mp3")
            mixer.music.play()
            put_markdown('## Bar Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose :",["day's VS Deaths and Confirmed","day's VS Deaths","day's VS Confirmed","end"])
                if tybar == "day's VS Deaths and Confirmed":
                    put_markdown("## day's VS Deaths and Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("deco.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    fig = go.Figure()
                    fig.add_trace(go.Bar(x=x,y=y,name="Deaths",marker_color='indianred'))
                    fig.add_trace(go.Bar(x=x,y=z,name="Confirmed",marker_color='lightsalmon'))
                    fig.update_layout(title=state+"'s Deaths and Confirmed From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Deaths and Confirmed",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
#https://pywebio.readthedocs.io/en/latest/
#https://pywebio-charts.pywebio.online/?app=plotly
                elif tybar == "day's VS Deaths":
                    put_markdown("## day's VS Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("death.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('indianred')
        #df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                    fig = px.bar(x=x,y=y,color_discrete_sequence=col)
                    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Deaths From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Deaths",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Confirmed":
                    put_markdown("## day's VS Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("con.mp3")
                    mixer.music.play()
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        #df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                    fig = px.bar(x=x,y=z,color_discrete_sequence=col)
                    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Confirmed From "+start+" To "+end,
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title="Confirmed",
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
        elif graphtype == 'Line':
            from pygame import mixer
            mixer.init()
            mixer.music.load("line.mp3")
            mixer.music.play()
            put_markdown('## Line Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Deaths and Confirmed","day's VS Deaths","day's VS Confirmed","end"])
                if tybar == "day's VS Deaths and Confirmed":
                    put_markdown("## day's VS Deaths and Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("deco.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    import plotly.graph_objects as go
        #df = px.data.gapminder().query("continent=='Oceania'")
        #fig = px.line(df,x=y, y=z,color_discrete_sequence=col )
                    fig = go.Figure()
                    fig.add_trace(go.Line(x=x,y=y,name='Deaths',marker_color='indianred'))
                    fig.add_trace(go.Line(x=x,y=z,name='Confirmed',marker_color='lightsalmon'))
                    fig.update_layout(title=state+"'s Deaths and Confirmed From "+start+" To "+end,
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Deaths and Confirmed',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(x=0,y=1.0,bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Deaths":
                    put_markdown("## day's VS Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("death.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('indianred')
        #df = px.data.gapminder().query("continent=='Oceania'")
                    fig = px.line(x=x, y=y,color_discrete_sequence=col )
                    fig.update_layout(title=state+"'s Deaths From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Deaths',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Confirmed":
                    put_markdown("## day's VS Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("con.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        #df = px.data.gapminder().query("continent=='Oceania'")
                    fig = px.line(x=x, y=z,color_discrete_sequence=col )
                    fig.update_layout(title=state+"'s Confirmed From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Confirmed',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == 'end':
                    i=1
        elif graphtype == 'Pie':
            from pygame import mixer
            mixer.init()
            mixer.music.load("pie.mp3")
            mixer.music.play()
            put_markdown('## Pie Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Deaths and Confirmed","day's VS Deaths","day's VS Confirmed","end"])
                if tybar == "day's VS Deaths and Confirmed":
                    put_markdown("## day's VS Deaths and Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("deco.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    from plotly.subplots import make_subplots
                    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
                    fig.add_trace(go.Pie(labels=x, values=y, name="Deaths"),1, 1)
                    fig.add_trace(go.Pie(labels=x, values=z, name="Confirmed"),1, 2)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title_text=state+"'s Deaths and Confirmed From "+start+" To "+end)
            
        # Add annotations in the center of the donut pies.
            
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Deaths":
                    put_markdown("## day's VS Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("death.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
        #df = px.data.gapminder().query("continent == 'Asia'")
                    fig = px.pie(values=y, names=x)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Deaths From "+start+" To "+end)
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Confirmed":
                    put_markdown("## day's VS Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("con.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px
        #df = px.data.gapminder().query("continent == 'Asia'")
                    fig = px.pie(values=z, names=x)
                    fig.update_traces(textposition='inside')
                    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
                    fig.update_layout(title=state+"'s Confirmed From "+start+" To "+end)
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1
            
        elif graphtype == 'Scatter':
            from pygame import mixer
            mixer.init()
            mixer.music.load("scatter.mp3")
            mixer.music.play()
            put_markdown('## Scatter Graph')
            time.sleep(2)
            i=0
            while i==0:
                time.sleep(3)
                from pygame import mixer
                mixer.init()
                mixer.music.load("choose.mp3")
                mixer.music.play()
                tybar=select("Choose : ",["day's VS Deaths and Confirmed","day's VS Deaths","day's VS Confirmed","end"])
                if tybar == "day's VS Deaths and Confirmed":
                    put_markdown("## day's VS Deaths and Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("deco.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.graph_objects as go
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=y,y=x,name='Deaths',
                    marker=dict(
                    color='rgba(156, 165, 196, 0.95)',
                    line_color='rgba(156, 165, 196, 1.0)',
                    )
                    ))
                    fig.add_trace(go.Scatter(x=z, y=x,name='Confirmed',
                    marker=dict(
                    color='rgba(204, 204, 204, 0.95)',
                    line_color='rgba(217, 217, 217, 1.0)'
                    )
                    ))

                    fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=10))
    
                    fig.update_layout(
                    title=state+"'s Deaths and Confirmed From "+start+" To "+end,
                    margin=dict(l=140, r=40, b=50, t=80),
                    legend=dict(
                    font_size=10,
                    yanchor='middle',
                    xanchor='right',
                    ),
                    width=800,
                    height=600,
                    paper_bgcolor='white',
                    plot_bgcolor='white',
                    hovermode='closest',
                    )
                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Deaths":
                    put_markdown("## day's VS Deaths")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("death.mp3")
                    mixer.music.play()
                    from pywebio.output import put_html
                    import plotly.express as px

        #df = pd.DataFrame(dict(school=x, salary=y,gender=x))
                    col=[]
                    for i in x:
                        col.append('indianred')
        # Use column names of df for the different parameters x, y, color, ...
                    fig = px.scatter(x=x, y=y,color_discrete_sequence=col,
                     title=state+"'s Deaths From "+start+" To "+end,
                     labels={"x":"day's","y":"Deaths"} # customize axis label
                    )

                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "day's VS Confirmed":
                    put_markdown("## day's VS Confirmed")
                    from pygame import mixer
                    mixer.init()
                    mixer.music.load("con.mp3")
                    from pywebio.output import put_html
                    import plotly.express as px
                    
        #df = pd.DataFrame(dict(school=x, salary=y,gender=x))
                    col=[]
                    for i in x:
                        col.append('lightsalmon')
        # Use column names of df for the different parameters x, y, color, ...
                    fig = px.scatter(x=x, y=z,color_discrete_sequence=col,
                     title=state+"'s Confirmed From "+start+" To "+end)
                    fig.update_layout(title=state+"'s Confirmed From "+start+" To "+end,
        #https://plotly.com/python/discrete-color/
        
                    xaxis_tickfont_size=14,
                    xaxis=dict(
                    title='days',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    yaxis=dict(
                    title='Confirmed',
                    titlefont_size=16,
                    tickfont_size=14,
                    ),
                    legend=dict(
                    x=0,
                    y=1.0,
                    bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'
                    ),
                    barmode='group',
                    bargap=0.15, # gap between bars of adjacent location coordinates.
                    bargroupgap=0.1 # gap between bars of the same location coordinate.
                    )

                    html = fig.to_html(include_plotlyjs="require", full_html=False)
                    put_html(html)
                    i=0
                elif tybar == "end":
                    i=1

# Use column names of df for the different parameters x, y, color, ...
            
            

        elif graphtype == 'Table':
            from pygame import mixer
            mixer.init()
            mixer.music.load("table.mp3")
            mixer.music.play()
            put_markdown('## Table')
            time.sleep(2)
            from pywebio.output import put_html
            import plotly.graph_objects as go
            from plotly.colors import n_colors
            np.random.seed(1)

            colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
            a = x
            b = y
            c = z
            headerColor = 'grey'
            col=[]
            for i in x:
                col.append('white')
            fig = go.Figure(data=[go.Table(
            header=dict(
            values=['<b>days</b>', '<b>Deaths</b>', '<b>Confirmed</b>'],
            line_color='darkslategray',fill_color='white',
            align='center',font=dict(color='black', size=12)
            ),
            cells=dict(
            values=[a, b, c],
            line_color='darkslategray',
            fill_color =col,
            align='center', font=dict(color='black', size=11)
            ))
            ])

            html = fig.to_html(include_plotlyjs="require", full_html=False)
            put_html(html)
            
def mltom():
    df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
    #put_text(df.head(10))

    country = df['Country'].unique()
    from pygame import mixer
    mixer.init()
    mixer.music.load("country.mp3")
    mixer.music.play()
    user_info=select("Choose The Country",country)#radio
    date = df["Date_reported"].unique()
    from pygame import mixer
    mixer.init()
    mixer.music.load("date.mp3")
    mixer.music.play()
    start = select("Start Date：",date)
    put_info('Start Date: ',start)
    from pygame import mixer
    mixer.init()
    mixer.music.load("date1.mp3")
    mixer.music.play()
    end = select("End Date：",date)
    put_info('End Date: ',end)
    df_c = df[df.Country == user_info ]
    sep_c =  df_c.loc[(df_c["Date_reported"] >= start) & (df_c["Date_reported"] <= end)]
    x = sep_c["Date_reported"]
    y = sep_c["New_cases"]
    z = sep_c["New_deaths"]

#preparing data
    data = sep_c["New_cases"]
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(data.values.reshape(-1,1))

#training the data
    from pygame import mixer
    mixer.init()
    mixer.music.load("test.mp3")
    mixer.music.play()
    put_success('Testing the data.....................')
    predicion_days = 60
    x_train= []
    y_train = []
    for x in range(predicion_days,len(scaled_data)):
        x_train.append(scaled_data[x-predicion_days:x,0])
        y_train.append(scaled_data[x,0])
    x_train,y_train=np.array(x_train),np.array(y_train)
    x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))


#creating prediction network
    model = Sequential()
    model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train[1].shape[1],1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))


    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train,y_train,epochs=25,batch_size=32)

#testing the model

    test_start = start
    test_end = end
    test_data =data
    actual_prices = data
    total_dataset = pd.concat((data,test_data),axis=0)

    model_inputs = total_dataset[len(total_dataset) - len(test_data) - predicion_days:].values
    model_inputs = model_inputs.reshape(-1,1)
    model_inputs = scaler.fit_transform(model_inputs)

    x_test = []
    for x in range(predicion_days, len(model_inputs)):
        x_test.append(model_inputs[x-predicion_days:x,0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

#predicting the data
    prediction_prices = model.predict(x_test)
    prediction_prices = scaler.inverse_transform(prediction_prices)


#predict next day
    from pygame import mixer
    mixer.init()
    mixer.music.load("pre.mp3")
    mixer.music.play()
    put_success('Predicting Next Day cases')
    time.sleep(2)
    real_data = [model_inputs[len(model_inputs) + 1 - predicion_days:len(model_inputs) + 1,0]]
    real_data = np.array(real_data)
    real_data = np.reshape(real_data,(real_data.shape[0],real_data.shape[1],1))

    prediction = model.predict(real_data)
    predict = scaler.inverse_transform(prediction)

    prediction_prices_len =len(prediction_prices)
    comparing = prediction_prices[prediction_prices_len - 1]
    put_info('Tomorrow cases will be : ',int(predict))
    combine = 'covid - 19'
    if comparing >= predict:
        from pygame import mixer
        mixer.init()
        mixer.music.load("tom.mp3")
        mixer.music.play()
        popup(combine , 'Tomorrow"S cases will be less than today')
        time.sleep(4)
    else:
        from pygame import mixer
        mixer.init()
        mixer.music.load("tomm.mp3")
        mixer.music.play()
        popup(combine , 'Tomorrow"S cases will be greater than today')
        time.sleep(4)







if __name__ == '__main__':
#https://towardsdatascience.com/pywebio-write-interactive-web-app-in-script-way-using-python-14f50155af4e
#https://pywebio.readthedocs.io/en/latest/output.html#pywebio.output.put_image
#https://www.tutorialspoint.com/python/tk_fonts.htm
    put_image(open('logo.jpg', 'rb').read())
    put_image(open('logo6.png', 'rb').read())
    put_text('\n')
    put_image(open('cc.jpg', 'rb').read())
    
    def run(string):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]')
        if(regex.search(string) == None):
            return True
        else:
            return False
    i=0
    put_text('\n')
    from pygame import mixer
    mixer.init()
    mixer.music.load("what.mp3")
    mixer.music.play()
    while i==0:
        name=input("What Is Your Name?")
        if(not name):
            toast('Should Not Be Empty',color='red')
            from pygame import mixer
            mixer.init()
            mixer.music.load("name.mp3")
            mixer.music.play()
        else:
            if run(name)== False:
                toast("Name Should Be In Alphabet's Can Not Contain Any Special Character's Or Numerical's")
                from pygame import mixer
                mixer.init()
                mixer.music.load("whatis.mp3")
                mixer.music.play()
            else:
                i=1
    i=0
    from pygame import mixer
    mixer.init()
    mixer.music.load("ageis.mp3")
    mixer.music.play()
    while i==0:
        age=input_group('What Is Your age?',[input(name='age',type=FLOAT)])
        if(not age['age']):
            toast('Should Not Be Empty',color='red')
            from pygame import mixer
            mixer.init()
            mixer.music.load("name.mp3")
            mixer.music.play()
        elif not type(age['age']) == int:
            toast("Age Should Be In Numerical's Can Not Contain Any Special Character's or Alphabet's")
            from pygame import mixer
            mixer.init()
            mixer.music.load("age.mp3")
            mixer.music.play()
        elif age['age'] <= 0:
            toast("Age Should Be In Numerical's Can Not Contain Any Special Character's or Alphabet's")
            from pygame import mixer
            mixer.init()
            mixer.music.load("age.mp3")
            mixer.music.play()
        else:
            i=1
    if age['age']<=18:
        from pygame import mixer
        mixer.init()
        mixer.music.load("sorry.mp3")
        mixer.music.play()
        toast("Sorry,"+name+" You Can't Access Our Website",color='red')
        time.sleep(3)
        
    else:
        from pygame import mixer
        mixer.init()
        mixer.music.load("congrats.mp3")
        mixer.music.play()
        toast("Congrats,"+name+" You Can Use Our Website!")#put_success
        time.sleep(3)
        #put_text("\n\n")
        #put_info('Hi, Welcome To Our Website '+ name)        
        #put_image(open('data2.jpg', 'rb').read(),width='180px', height='180px')
        put_text('\n')
        put_image(open('om.jpeg', 'rb').read(),width='150px', height='150px')
        from pygame import mixer
        mixer.init()
        mixer.music.load("my.mp3")
        mixer.music.play()
        put_markdown('## myself:kolla.om vivek,BE-CSE,3rd year')
        time.sleep(5)
        i=0
        while i==0:
            from pygame import mixer
            mixer.init()
            mixer.music.load("which.mp3")
            mixer.music.play()
            app = select("Which One Do You Want To Go For : ",["All Countries","India (state's)","Predicting Next Day Covid Case's"])
            if app == "All Countries":
                covid_app()
            elif app == "India (state's)":
                india_app()
            elif app == "Predicting Next Day Covid Case's":
                mltom()
            #time.sleep(1)
            from pygame import mixer
            mixer.init()
            mixer.music.load("do.mp3")
            mixer.music.play()
            rad=radio("Do You Want To Continue",options=['yes','no'])
            if rad=='yes':
                i=0
            else:
                i=1
from pygame import mixer
mixer.init()
mixer.music.load("stay.mp3")
mixer.music.play()
toast('Stay Home , Stay Safe')
time.sleep(2)
from pygame import mixer
mixer.init()
mixer.music.load("thanks.mp3")
mixer.music.play()
toast('Thanks, For visiting our web-site!')#put_success
time.sleep(3)
#pywebio.output.clear()
clear(scope=None)
from pygame import mixer
mixer.init()
mixer.music.load("fur.mp3")
mixer.music.play()
put_markdown("# Further Covid-19 Related information is below :")
put_link("MOHFW Main Website", url="https://www.mohfw.gov.in/", app=None, new_window=True, scope=None)
put_text("\n")
put_link("Covid-19 Live Dashboard", url="https://news.google.com/covid19/map?hl=en-IN&mid=%2Fm%2F03rk0&gl=IN&ceid=IN%3Aen", app=None, new_window=True, scope=None)
put_text("\n")
put_link("covid-19 contact tracing app for India", url="https://play.google.com/store/apps/details?id=nic.goi.aarogyasetu", app=None, new_window=True, scope=None)
put_text("\n")
put_link("Andhra Pradesh sachivalayam center for vaccination ", url="https://www.google.com/search?client=ms-android-samsung-ss&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=AOaemvKwTWIbtpoT477Nv6bq0hhz4nGLNA:1636384621085&q=ap+sachivalayam+center&rflfq=1&num=10&ved=2ahUKEwjPybjgh4n0AhVX7nMBHVeNACEQtgN6BAgREAc#rlfi=hd:;si:;mv:[[17.9456331,83.5551527],[14.2120362,77.1918017]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2", app=None, new_window=True, scope=None)
put_text("\n")
put_info("""To prevent the spread of COVID-19:
 -> Maintain a safe distance from others (at least 1 metre), even if they don’t appear to be sick.
 -> Wear a mask in public, especially indoors or when physical distancing is not possible.
 -> Choose open, well-ventilated spaces over closed ones. Open a window if indoors.
 -> Clean your hands often. Use soap and water, or an alcohol-based hand rub.
 -> Get vaccinated when it’s your turn. Follow local guidance about vaccination.
 -> Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
 -> Stay home if you feel unwell.""")
