from pathlib import Path

import matplotlib.pyplot as plt

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
# 1. Load Dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("Original Shape:", X.shape)


# --------------------------------------------------
# 2. Scale Features
# --------------------------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# --------------------------------------------------
# 3. Apply PCA
# --------------------------------------------------

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

print("\nTransformed Shape:", X_pca.shape)


# --------------------------------------------------
# 4. Explained Variance
# --------------------------------------------------

variance_ratio = pca.explained_variance_ratio_

print("\nExplained Variance Ratio:")
print(variance_ratio)

print("\nTotal Variance Captured:")
print(f"{variance_ratio.sum() * 100:.2f}%")


# --------------------------------------------------
# 5. Visualize PCA
# --------------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y,
    cmap="viridis",
    s=60
)

plt.title("Iris Dataset - PCA (2 Components)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.tight_layout()

plt.savefig(GRAPH_DIR / "pca_visualization.png")
plt.show()


# --------------------------------------------------
# 6. Explained Variance Plot
# --------------------------------------------------

plt.figure(figsize=(8, 5))

components = ["PC1", "PC2"]

plt.bar(components, variance_ratio)

plt.title("Explained Variance by PCA Components")
plt.ylabel("Variance Explained")
plt.xlabel("Principal Components")

plt.tight_layout()

plt.savefig(GRAPH_DIR / "pca_variance.png")
plt.show()


print("\nPCA graphs saved in:", GRAPH_DIR)