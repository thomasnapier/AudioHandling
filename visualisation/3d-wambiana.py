import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
feature_vectors = pd.read_csv("39-features-wambiana.csv")
labels_true = feature_vectors["class"]

feature_vectors["class"] = feature_vectors["class"].str.replace('other', str(0))
feature_vectors["class"] = feature_vectors["class"].str.replace('biophony', str(1))
feature_vectors["class"] = feature_vectors["class"].str.replace('geophony', str(2))
feature_vectors["class"] = feature_vectors["class"].str.replace('anthrophony', str(3))
y_km = feature_vectors["class"]
y_km = y_km.values

feature_vectors = feature_vectors.drop(columns=["class"])
feature_vectors = feature_vectors.iloc[:, 0:13].values
feature_vectors

model = TSNE(n_components=3, learning_rate=150, perplexity=50, verbose=2, angle=0.1, random_state=0).fit_transform(feature_vectors)

colors = ['r', 'g', 'b', 'y']
y_int = [int(label) for label in y_km]
# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(model[:, 0], model[:, 1], model[:, 2], c=[colors[label] for label in y_int])

# Set the viewing angle of the plot
ax.view_init(elev=20, azim=35)

# Allow interactive rotation of the plot
ax.set_box_aspect([1,1,1])
ax.mouse_init()

# Show plot
plt.show()
