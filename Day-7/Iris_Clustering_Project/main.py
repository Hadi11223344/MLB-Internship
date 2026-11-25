from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# --------------------------------------------------
# Paths
# --------------------------------------------------

DAY7_DIR = Path(__file__).resolve().parents[1]
GRAPH_DIR = DAY7_DIR / "Graphs"

GRAPH_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 1. Load Data
# --------------------------------------------------

iris = load_iris(as_frame=True)

X = iris.data
y = iris.target

print("=" * 60)
print("IRIS CLUSTERING MINI-PROJECT")
print("=" * 60)

print("\nDataset Shape:", X.shape)


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


plt.figure(figsize=(8, 5))

plt.plot(k_values, inertias, marker="o")

plt.title("Elbow Method - Iris")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Within-Cluster Squared Distance")

plt.xticks(k_values)
plt.grid(True)

plt.tight_layout()

plt.savefig(GRAPH_DIR / "project_elbow.png")
plt.show()


# --------------------------------------------------
# 4. Train K-Means
# --------------------------------------------------

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

print("\nK-Means trained successfully!")
print("\nCluster Counts:")

print(pd.Series(clusters).value_counts().sort_index())


# --------------------------------------------------
# 5. PCA - Reduce to 2 Dimensions
# --------------------------------------------------

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

variance = pca.explained_variance_ratio_

print("\nPCA Explained Variance:")

print(f"PC1: {variance[0] * 100:.2f}%")
print(f"PC2: {variance[1] * 100:.2f}%")

print(
    f"Total: {variance.sum() * 100:.2f}%"
)


# --------------------------------------------------
# 6. Visualize K-Means Clusters using PCA
# --------------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=clusters,
    cmap="viridis",
    s=60
)

plt.title("K-Means Clusters Visualized using PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.tight_layout()

plt.savefig(GRAPH_DIR / "project_clusters_pca.png")
plt.show()


# --------------------------------------------------
# 7. Visualize Actual Species using PCA
# --------------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y,
    cmap="viridis",
    s=60
)

plt.title("Actual Iris Species Visualized using PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.tight_layout()

plt.savefig(GRAPH_DIR / "project_species_pca.png")
plt.show()


# --------------------------------------------------
# 8. Compare Clusters with Actual Species
# --------------------------------------------------

comparison = pd.crosstab(
    pd.Series(clusters, name="K-Means Cluster"),
    pd.Series(
        iris.target_names[y],
        name="Actual Species"
    )
)

print("\nCluster vs Actual Species:")

print(comparison)


# --------------------------------------------------
# 9. Final Results
# --------------------------------------------------

print("\nFinal Inertia:")
print(kmeans.inertia_)

print("\nProject completed successfully!")

print("\nGraphs saved in:", GRAPH_DIR)