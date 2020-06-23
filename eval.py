import pandas as pd
import plotly
#pd.options.plotting.backend = 'plotly'
#import matplotlib
#import plotly as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from pathlib import Path
path = Path('data\\data_rt50_multi.csv')
df = pd.read_csv(path, sep = ';', dtype = 'str', index_col=0)
fig = make_subplots(rows = len(df.columns), cols=1, subplot_titles=df.columns)
num = 1
for i in df.columns:
    data = df[i].value_counts(normalize=True)
    x= pd.Series(data.index, dtype=str)
    fig.add_trace(go.Bar(x=x, y=data.values, name=i), row = num, col =1)
    fig.update_xaxes(type="category",categoryorder="category ascending", row = num, col =1)
    num = num + 1
   
fig.update_layout(height= num*800, showlegend=False)
fig.show() 
