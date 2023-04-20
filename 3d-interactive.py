import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly
from itertools import cycle
import pygame

# Read in data from CSV file
df = pd.read_csv('combined-3d.csv')

# Initialize Pygame mixer for playing audio
pygame.mixer.init()

colors = cycle(plotly.colors.sequential.Rainbow)
fig = go.Figure()
for c in df['class'].unique():
    dfi = df[df['class'] == c]
    fig.add_trace(go.Scatter3d(x=dfi['x'], y = dfi['y'], z = dfi['z'],
                               mode = 'markers',
                               name = c,
                               customdata = dfi['sound_path'],
                               marker=dict(
                                        size=2),
                               marker_color = next(colors)))
    
# Define app and layout using Dash
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id='scatter-plot', figure=fig)
])

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Define on-click functionality for scatter plot
@app.callback(Output('scatter-plot', 'figure'), Input('scatter-plot', 'clickData'))
def on_click(clickData):
    print(clickData)
    play_sound(clickData['points'][0]['customdata'])
    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)



## working - mostly
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# import pandas as pd
# import mplcursors
# import plotly.express as px
# import plotly.graph_objects as go
# import plotly
# from itertools import cycle


# colors = cycle(plotly.colors.sequential.Rainbow)

# # Read in the CSV file
# df = pd.read_csv('combined-3d.csv')

# fig = go.Figure()
# for c in df['class'].unique():
#     dfi = df[df['class'] == c]
#     fig.add_trace(go.Scatter3d(x=dfi['x'], y = dfi['y'], z = dfi['z'],
#                                mode = 'markers',
#                                name = c,
#                                marker=dict(
#                                         size=2),
#                                marker_color = next(colors)))


# fig.show()






# fig = go.Figure(data=[go.Scatter3d(x=df['x'], y=df['y'], z=df['z'], customdata=["class"], 
#                                    mode='markers',
#                                    marker=dict(
#                                         size=2,
#                                         color=df['class'],
#                                         colorscale='Viridis'
#                                    ))])

# fig.show()