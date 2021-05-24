import pandas as pd
import plotly.express as px
import csv
import plotly.figure_factory as ff

data = pd.read_csv('ratings.csv')
graph = ff.create_distplot([data["Avg Rating"].tolist()], ["Mobile Brand"])
graph.show()