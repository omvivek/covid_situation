
'''from gtts import gTTS
mytext = "Further Covid-19 Related information is below"
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("fur.mp3")'''
from covid_india import states
from matplotlib import pyplot as plt
from pywebio.output import put_html
import plotly.graph_objects as go
import plotly.express as px
from pywebio.input import * 
from pywebio.output import *
def today_india():
    x=[]
    y=["Andaman and Nicobar Islands",'Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat', 'Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala***','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur', 'Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim', 'Tamil Nadu','Telangana','Tripura', 'Uttarakhand','Uttar Pradesh','West Bengal']
    for i in y:
        st=states.getdata(i)['Active']
        x.append(st)
    put_text(x)
    col=[]
    for i in y:
        col.append('indianred')
    fig = px.bar(x=x,y=y,color_discrete_sequence=col)
                    #fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.update_layout(title="India"+"'s Cases ",
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
                    
today_india()
