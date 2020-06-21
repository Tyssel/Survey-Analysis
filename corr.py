import pandas as pd
import plotly
#pd.options.plotting.backend = 'plotly'
#import matplotlib
#import plotly as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from pathlib import Path
path = Path('C:\\Users\\tonis\\Documents\\GitHub\\SurveyAnalysis\\Survey-Analysis\\Dati-Road-to-50.csv')
df = pd.read_csv(path, sep = ';', dtype = 'str', header=0, index_col=0)
#print(df.columns)
print(df.corr())