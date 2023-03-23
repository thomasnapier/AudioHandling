import matplotlib.pyplot as plt
import webbrowser
from tkinter import *
from matplotlib.widgets import RadioButtons
import pandas as pd

# Define x and y coordinates and file paths for each point
# data = pd.read_csv('tsne.csv')
# x=data[data.columns[0]]
# y=data[data.columns[1]]
# define the data
data = {'x': [1, 2, 3, 4, 5],
        'y': [2, 3, 1, 4, 5],
        'category': ['A', 'B', 'A', 'B', 'A']}

# map categories to colors
colors = {'A': 'red', 'B': 'blue'}
data['colors'] = [colors[category] for category in data['category']]

# create the figure and axes
fig, ax = plt.subplots()

# create the scatter plot
scatter = ax.scatter(data['x'], data['y'], c=data['colors'])

# create the radio button widget
category_radio = plt.widgets.RadioButtons(ax=[plt.axes([0.05, 0.7, 0.1, 0.25]),
                                               plt.axes([0.05, 0.4, 0.1, 0.25])],
                                          labels=['A', 'B'])

# define the function to be called when a radio button is clicked
def radio_button_clicked(label):
    # update the category for the selected points
    indices = scatter.get_offsets()[:,0].tolist().index(scatter.get_offsets()[:,0][scatter.get_array()==1])
    data['category'][indices] = label
    # update the color of the selected points
    data['colors'] = [colors[category] for category in data['category']]
    scatter.set_color(data['colors'])
    # redraw the plot
    fig.canvas.draw()

# connect the radio button widget to the function
category_radio.on_clicked(radio_button_clicked)

plt.show()