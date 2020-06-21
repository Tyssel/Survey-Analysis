import pandas as pd
import plotly
#pd.options.plotting.backend = 'plotly'
#import matplotlib
#import plotly as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from pathlib import Path
path = Path('data\\data_rt50_general.csv')
df = pd.read_csv(path, sep = ';', dtype = 'str', index_col=0)
fig = make_subplots(rows = len(df.columns), cols=1, subplot_titles=df.columns)
num = 1
for i in df.columns:
    data = df[i].value_counts(normalize=True)
    fig.add_trace(go.Bar(x=data.index, y=data.values, name=i), row = num, col =1)
    num = num + 1
    #if num == 20:
    #    break
fig.update_layout(height= num*1000, showlegend=False)
fig.show() 
