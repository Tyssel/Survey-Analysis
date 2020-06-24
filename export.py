import pandas as pd
import plotly
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from pathlib import Path
path = Path('data\\data_rt50_general.csv')
df = pd.read_csv(path, sep = ';', dtype = 'str', index_col=0)
fig = go.Figure()
num = 1
if not os.path.exists("images/pie"):
    os.mkdir("images/pie")
   
for i in df.columns:
    data = df.groupby('A2 – Genere')[i].value_counts(normalize=True)
    #data = df[i].value_counts(normalize=True)
    #x= pd.Series(data.index, dtype=str)
    data_m = data['M']
    data_f = data['F']
    fig.add_trace(go.Pie(labels=data_m.index, values=data_m.values, name= 'm'))
    #fig.add_trace(go.Pie(labels=data_f.index, values=data_f.values, name='f'))
    #fig.update_layout(title_text= i)
    #fig.update_xaxes(type="category",categoryorder="category ascending")
    fig.write_image("images/Pie/"+ str(num) +"_pie_male.jpeg")
    num = num + 1
    fig = go.Figure()