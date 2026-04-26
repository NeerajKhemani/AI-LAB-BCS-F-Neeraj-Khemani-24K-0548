import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('marketing_campaign.csv', sep='\t')
print(df.head())
print(f"\nDataset Shape: {df.shape}")

features = ['Income', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'NumWebPurchases', 'NumStorePurchases']

x = df[features].copy()
print(features)

print("\nMissing Values before handling:\n", x.isnull().sum())
x['Income'] = x['Income'].fillna(x['Income'].median())
print("\nMissing Values after handling:\n", x.isnull().sum())


scaler   = StandardScaler()
X_scaled = scaler.fit_transform(x)
print("\nStandard Scaling applied to all selected features.")

wcss_list = []

for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss_list.append(kmeans.inertia_)

mtp.plot(range(2, 11), wcss_list)
mtp.title('The Elbow Method Graph')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

print("\nWCSS Values")
for k, wcss in zip(range(2, 11), wcss_list):
    print(f"  K={k:>2} -> WCSS: {wcss:>12.2f}")

print("\nOptimal K selected: 4 ")

kmeans    = KMeans(n_clusters=4, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(X_scaled)


df['Cluster'] = y_predict

x_raw = x.values

mtp.scatter(x_raw[y_predict == 0, 0], x_raw[y_predict == 0, 2], s=100, c='blue',   label='Cluster 1')  #for first cluster
mtp.scatter(x_raw[y_predict == 1, 0], x_raw[y_predict == 1, 2], s=100, c='green',  label='Cluster 2')  #for second cluster
mtp.scatter(x_raw[y_predict == 2, 0], x_raw[y_predict == 2, 2], s=100, c='red',    label='Cluster 3')  #for third cluster
mtp.scatter(x_raw[y_predict == 3, 0], x_raw[y_predict == 3, 2], s=100, c='purple', label='Cluster 4')  #for fourth cluster
mtp.scatter(
    scaler.inverse_transform(kmeans.cluster_centers_)[:, 0],
    scaler.inverse_transform(kmeans.cluster_centers_)[:, 2],
    s=300, c='yellow', label='Centroid'
)
mtp.title('Clusters of customers')
mtp.xlabel('Annual Income ($)')
mtp.ylabel('Amount Spent on Wines ($)')
mtp.legend()
mtp.show()

print("\nFinal Dataset with Cluster Labels")
print(df[['ID', 'Income', 'MntWines', 'MntMeatProducts', 'Cluster']].head(20).to_string())

print("\nCluster Summary (Mean Values)")
print(df.groupby('Cluster')[features].mean().round(1).to_string())
