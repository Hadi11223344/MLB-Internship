# Day 7 — Unsupervised Learning, K-Means & PCA

## Objectives

- Understand Unsupervised Learning and Clustering.
- Learn the K-Means algorithm and centroid-based grouping.
- Understand convergence and cluster inertia.
- Explore the Elbow Method for selecting K.
- Understand why feature scaling matters for distance-based algorithms.
- Learn Principal Component Analysis (PCA).
- Reduce dimensionality from 4 features to 2.
- Visualize clustering results.
- Compare discovered clusters against actual Iris species.

## Dataset

The Iris dataset from Scikit-learn was used.

- Samples: 150
- Features: 4
- Species: 3
- Missing values: None

## Concepts Covered

### K-Means

K-Means partitions observations into K clusters by repeatedly assigning observations to their nearest centroid and recalculating the centroids until convergence.

### Elbow Method

The Elbow Method compares the within-cluster squared distances across different values of K to identify a point where additional clusters provide diminishing improvements.

### Feature Scaling

StandardScaler was used to standardize features before distance-based clustering.

### PCA

Principal Component Analysis reduced the original four features to two principal components for visualization.

## PCA Results

- PC1: 72.96%
- PC2: 22.85%
- Total variance retained: 95.81%

## Clustering Results

K-Means was trained with K=3.

| Cluster | Samples |
|---|---:|
| Cluster 0 | 53 |
| Cluster 1 | 50 |
| Cluster 2 | 47 |

### Cluster vs Actual Species

| Cluster | Setosa | Versicolor | Virginica |
|---|---:|---:|---:|
| 0 | 0 | 39 | 14 |
| 1 | 50 | 0 | 0 |
| 2 | 0 | 11 | 36 |

Cluster 1 perfectly captured all 50 Setosa samples. The remaining two clusters separated Versicolor and Virginica reasonably well but contained some overlap.

A simple majority-species alignment yielded 125/150 matching observations (83.33%). This is an illustrative comparison rather than a formal supervised evaluation.

## Scripts

- `KMeans_Clustering/main.py` — K-Means and Elbow Method.
- `PCA/main.py` — PCA dimensionality reduction and visualization.
- `Iris_Clustering_Project/main.py` — Integrated clustering, PCA visualization and comparison.

## Graphs

- `elbow_curve.png`
- `kmeans_clusters.png`
- `pca_visualization.png`
- `pca_variance.png`
- `project_elbow.png`
- `project_clusters_pca.png`
- `project_species_pca.png`

## Key Learning

Unsupervised learning can discover structure in data without target labels. K-Means groups observations according to distance, while PCA reduces dimensions by finding directions that capture the greatest variance.

This exercise demonstrated clustering, dimensionality reduction, visualization and comparison of discovered patterns against known labels.