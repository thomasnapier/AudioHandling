import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import pandas as pd
import pygame

# Load data from a CSV file
data = pd.read_csv('tsne-wambiana.csv')

# Initialize Pygame mixer for playing audio
pygame.mixer.init()

# Define a function to play the sound clip for a given point
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Define a function to update the class label for a given point
def update_label(text, index):
    data.iloc[index]['class_label'] = text

# Define a function to handle button clicks
def button_click(event):
    if event.inaxes is not None:
        index = int(event.xdata)
        play_sound(data.iloc[index]['sound_file'])
        textbox.set_val(data.iloc[index]['class_label'])
        textbox.index = index
        update_plot()

# Define a function to handle text box changes
def textbox_submit(text):
    index = textbox.index
    update_label(text, index)
    data.to_excel('data_updated.xlsx', index=False)
    update_plot()

# Define a function to update the plot
def update_plot():
    fig, ax = plt.subplots()
    ax.set_title('Interactive Scatterplot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')

    # Group the data by class label
    grouped_data = data.groupby('class_label')

    # Define a color map for the class labels
    colormap = plt.cm.get_cmap('hsv', len(grouped_data))

    # Plot each group with a different color
    for i, (label, group) in enumerate(grouped_data):
        color = colormap(i)
        ax.scatter(group['x'], group['y'], label=label, color=color, picker=5)

    # Add button and text box
    button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])
    play_button = Button(button_ax, 'Play')

    textbox_ax = plt.axes([0.1, 0.05, 0.5, 0.075])
    initial_text = data.iloc[0]['class_label']
    textbox = TextBox(textbox_ax, 'Class Label', initial=initial_text)
    textbox.index = None  # Initialize index attribute to None
    textbox.on_submit(textbox_submit)

    # Add button click event handler
    play_button.on_clicked(button_click)

    # Draw an outline around the clicked point
    if textbox.index is not None:
        clicked_point = data.iloc[textbox.index]
        ax.scatter(clicked_point['x'], clicked_point['y'], color='none', edgecolor='black', linewidth=2, picker=5)

    # Add pick event handler to select a point
    def on_pick(event):
        nonlocal textbox  # Make the textbox variable accessible inside the function
        index = event.ind[0]
        play_sound(data.iloc[index]['sound_file'])
        textbox.set_val(data.iloc[index]['class_label'])
        textbox.index = index

        # Remove previous outlines and draw new outline around selected point
        for artist in ax.lines + ax.collections:
            if artist.get_linewidth() == 2:
                artist.set_linewidth(0)
        event.artist.set_linewidth(2)

        # Save the updated label
        data.iloc[index]['class_label'] = textbox.text
        data.to_excel('data_updated.xlsx', index=False)

        update_plot()

    fig.canvas.mpl_connect('pick_event', on_pick)

update_plot()
plt.show()
