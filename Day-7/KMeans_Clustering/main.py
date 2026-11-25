from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler


# --------------------------------------------------
# Paths
# --------------------------------------------------

DAY7_DIR = Path(__file__).resolve().parents[1]
GRAPH_DIR = DAY7_DIR / "Graphs"
GRAPH_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
feature_names = iris.feature_names

print("Dataset Shape:", X.shape)


# --------------------------------------------------
# 2. Scale Features
# --------------------------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nFeatures scaled successfully!")


# --------------------------------------------------
# 3. Elbow Method
# --------------------------------------------------

inertias = []
k_values = range(1, 11)

for k in k_values:

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    inertias.append(model.inertia_)

    print(f"K={k} | Inertia={model.inertia_:.2f}")


# Plot Elbow Curve

plt.figure(figsize=(8, 5))

plt.plot(k_values, inertias, marker="o")

plt.title("Elbow Method - Iris Dataset")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.xticks(k_values)
plt.grid(True)

plt.tight_layout()

plt.savefig(GRAPH_DIR / "elbow_curve.png")
plt.show()


# --------------------------------------------------
# 4. K-Means with K=3
# --------------------------------------------------

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

cluster_labels = kmeans.fit_predict(X_scaled)

print("\nCluster Assignments:")
print(cluster_labels)

print("\nCluster Centers (Scaled):")
print(kmeans.cluster_centers_)

print("\nFinal Inertia:")
print(kmeans.inertia_)


# --------------------------------------------------
# 5. Visualize Clusters using Petal Features
# --------------------------------------------------

# Petal length = feature index 2
# Petal width  = feature index 3

plt.figure(figsize=(8, 6))

plt.scatter(
    X_scaled[:, 2],
    X_scaled[:, 3],
    c=cluster_labels,
    cmap="viridis",
    s=60
)

plt.scatter(
    kmeans.cluster_centers_[:, 2],
    kmeans.cluster_centers_[:, 3],
    marker="X",
    s=250,
    color="red",
    edgecolor="black",
    label="Centroids"
)

plt.title("K-Means Clustering of Iris (K=3)")
plt.xlabel("Petal Length (Scaled)")
plt.ylabel("Petal Width (Scaled)")
plt.legend()

plt.tight_layout()

plt.savefig(GRAPH_DIR / "kmeans_clusters.png")
plt.show()


print("\nGraphs saved in:", GRAPH_DIR)