import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly
from itertools import cycle
import pygame
import csv

# Read in data from CSV file
df = pd.read_csv('umap-wambiana-3D.csv')

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

# keep legend readable and edit graph so it doesn't reset upon user interaction
fig.update_layout(legend= {'itemsizing': 'constant'}, uirevision="some value") 

# Define app and layout using Dash
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id='scatter-plot', figure=fig),
    dcc.Dropdown(id='class-label', options=[{'label': 'Anthrophony', 'value': 'anthrophony'},
                                               {'label': 'Biophony', 'value': 'biophony'},
                                                {'label': 'Geophony', 'value': 'geophony'},
                                                 {'label': 'Other', 'value': 'other'}])

                                                 #TODO: create options using list comprehension (https://community.plotly.com/t/preserving-ui-state-like-zoom-in-dcc-graph-with-uirevision-with-dash/15793)
])

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def update_csv(row, file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        header = rows[0]
        index = None
        for i, h in enumerate(header):
            if h == 'file_path':
                index = i
                break
        if index is None:
            raise ValueError('CSV file does not contain "file_path" column')
        for i, r in enumerate(rows[1:]):
            if r[index] == row[index]:
                for j in range(len(header)):
                    if row[j] != r[j]:
                        rows[i+1][j] = row[j]
                break
        else:
            rows.append(row)
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
# Define on-click functionality for scatter plot
@app.callback(Output('scatter-plot', 'figure'), Input('scatter-plot', 'clickData'))
def on_click(clickData):
    print(clickData)

    # play audio clip based on custom data field (sound path)
    play_sound(clickData['points'][0]['customdata'])
    return fig

@app.callback(Output('class-label', 'value'), Input('scatter-plot', 'clickData'))
def update_text(clickData):
    if clickData is None:
        return ''
    else:
        # find corresponding row of data based on clicked data point
        custom = clickData['points'][0]['customdata']
        row = df.loc[df['sound_path'] == custom]
        class_label = row['class']
        return class_label.values[0]
    


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