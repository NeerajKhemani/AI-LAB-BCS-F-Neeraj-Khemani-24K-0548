import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv('Mall_Customers.csv')
df.head()

print(df.head())
print(f"\nDataset Shape: {df.shape}")
print("\nColumn Names:", df.columns.tolist())
print("\nMissing Values:\n", df.isnull().sum())

le = LabelEncoder()
df['Gender_encoded'] = le.fit_transform(df['Genre'])   

x = df[['Gender_encoded', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']].values


print("\nCLUSTERING WITHOUT SCALING")

wcss_list = [] 

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)

mtp.plot(range(1, 11), wcss_list)
mtp.title('The Elbow Method Graph (Without Scaling)')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

kmeans     = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict  = kmeans.fit_predict(x)

mtp.scatter(x[y_predict == 0, 2], x[y_predict == 0, 3], s=100, c='blue',   label='Cluster 1')  #for first cluster
mtp.scatter(x[y_predict == 1, 2], x[y_predict == 1, 3], s=100, c='green',  label='Cluster 2')  #for second cluster
mtp.scatter(x[y_predict == 2, 2], x[y_predict == 2, 3], s=100, c='red',    label='Cluster 3')  #for third cluster
mtp.scatter(x[y_predict == 3, 2], x[y_predict == 3, 3], s=100, c='black',  label='Cluster 4')  #for fourth cluster
mtp.scatter(x[y_predict == 4, 2], x[y_predict == 4, 3], s=100, c='purple', label='Cluster 5')  #for fifth cluster
mtp.scatter(kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:, 3], s=300, c='yellow', label='Centroid')
mtp.title('Clusters of Customers (Without Scaling)')
mtp.xlabel('Annual Income (k$)')
mtp.ylabel('Spending Score (1-100)')
mtp.legend()
mtp.show()

print("Cluster labels (without scaling):", y_predict[:10])

print("\nCLUSTERING WITH SCALING (except Age)")

x_to_scale = df[['Gender_encoded', 'Annual Income (k$)', 'Spending Score (1-100)']].values
x_age      = df[['Age']].values

scaler    = StandardScaler()
X_scaled  = scaler.fit_transform(x_to_scale)
X_combined = nm.hstack([X_scaled, x_age])

wcss_list = []  

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_combined)
    wcss_list.append(kmeans.inertia_)

mtp.plot(range(1, 11), wcss_list)
mtp.title('The Elbow Method Graph (With Scaling except Age)')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

kmeans    = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(X_combined)

mtp.scatter(x[y_predict == 0, 2], x[y_predict == 0, 3], s=100, c='blue',   label='Cluster 1')  #for first cluster
mtp.scatter(x[y_predict == 1, 2], x[y_predict == 1, 3], s=100, c='green',  label='Cluster 2')  #for second cluster
mtp.scatter(x[y_predict == 2, 2], x[y_predict == 2, 3], s=100, c='red',    label='Cluster 3')  #for third cluster
mtp.scatter(x[y_predict == 3, 2], x[y_predict == 3, 3], s=100, c='black',  label='Cluster 4')  #for fourth cluster
mtp.scatter(x[y_predict == 4, 2], x[y_predict == 4, 3], s=100, c='purple', label='Cluster 5')  #for fifth cluster
mtp.title('Clusters of Customers (With Scaling except Age)')
mtp.xlabel('Annual Income (k$)')
mtp.ylabel('Spending Score (1-100)')
mtp.legend()
mtp.show()

print("Cluster labels (with scaling):", y_predict[:10])

## comparison:
##   WITHOUT Scaling:
##  - Annual Income (range: 15-150k) dominates the clustering because its magnitude is much larger than Spending Score (1-100) and Gender (0-1).
##  - Clusters are mainly driven by income differences, ignoring other features.

##  WITH Scaling (except Age):
##  - Gender, Annual Income, and Spending Score are all normalized to the same scale, so each contributes equally to the distance calculation.
##  - Age is kept unscaled as instructed, giving it moderate influence.
##  - Clusters are more balanced and meaningful, capturing patterns across multiple features rather than being dominated by one large-valued feature.

##  Scaling is critical when features have very different ranges.
##   It ensures K-Means treats all features fairly and produces better clusters.