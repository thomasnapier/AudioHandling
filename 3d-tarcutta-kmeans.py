import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
feature_vectors = pd.read_csv("39-feature-vector.csv")
labels_true = feature_vectors["class"]
feature_vectors = feature_vectors.drop(columns=["class"])
feature_vectors = feature_vectors.iloc[:, 0:13].values

kmeans_data_old = pd.read_csv('kmeans_results.csv')

#encoding class values
kmeans_data_old['class'] = kmeans_data_old['class'].str.replace('other', str(0))
kmeans_data_old['class'] = kmeans_data_old['class'].str.replace('biophony', str(1))
kmeans_data_old['class'] = kmeans_data_old['class'].str.replace('geophony', str(2))
kmeans_data_old['class'] = kmeans_data_old['class'].str.replace('anthrophony', str(3))

y_km = kmeans_data_old['class']
# y_km.drop(y_km.tail(1).index, inplace=True)
y_km = y_km.values

model = TSNE(n_components=3, learning_rate=150, perplexity=50, verbose=2, angle=0.1, random_state=0).fit_transform(feature_vectors)

from sklearn.cluster import KMeans
km = KMeans(n_clusters=8, init='k-means++', random_state=42)
y_km = km.fit_predict(model)
labels = km.labels_

colors = ['r', 'g', 'b', 'y', 'rx', 'c', 'm', 'k', 'w']
y_int = [int(label) for label in labels]
# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(model[:, 0], model[:, 1], model[:, 2], c=labels, cmap='viridis')

# Set the viewing angle of the plot
ax.view_init(elev=20, azim=35)

# Allow interactive rotation of the plot
ax.set_box_aspect([1,1,1])
ax.mouse_init()

# Show plot
plt.title("3D t-SNE graph with kmeans (k=8) overlayed")
plt.show()
