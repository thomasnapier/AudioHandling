# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# import pandas as pd
# import mplcursors
# import plotly.express as px

# # Read in the CSV file
# df = pd.read_csv('combined-3d.csv')

# fig = px.scatter_3d(df, x='x', y='y', z='z', custom_data=["class"],
#               color='class', size_max=18)

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import mplcursors
import plotly.express as px
import plotly.graph_objects as go
import plotly
import numpy as np
from itertools import cycle
colors = cycle(plotly.colors.sequential.Rainbow)

# Read in the CSV file
df = pd.read_csv('combined-3d.csv')

fig = go.Figure()
for c in df['class'].unique():
    dfi = df[df['class'] == c]
    fig.add_trace(go.Scatter3d(x=dfi['x'], y = dfi['y'], z = dfi['z'],
                               mode = 'markers',
                               name = c,
                               marker=dict(
                                        size=2),
                               marker_color = next(colors)))
fig.show()





# fig = go.Figure(data=[go.Scatter3d(x=df['x'], y=df['y'], z=df['z'], customdata=["class"], 
#                                    mode='markers',
#                                    marker=dict(
#                                         size=2,
#                                         color=df['class'],
#                                         colorscale='Viridis'
#                                    ))])

# fig.show()