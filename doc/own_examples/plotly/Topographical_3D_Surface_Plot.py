# Topographical_3D_Surface_Plot.py
# https://plotly.com/python/3d-surface-plots/

import plotly.graph_objects as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('mt_bruno_elevation.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()