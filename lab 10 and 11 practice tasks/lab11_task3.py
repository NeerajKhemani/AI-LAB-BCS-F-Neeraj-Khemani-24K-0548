import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('Student_performance_data _.csv')

print(df.head())
print(f"\nDataset Shape: {df.shape}")
print("\nColumn Names:", df.columns.tolist())

if 'StudentID' not in df.columns:
    df.insert(0, 'StudentID', range(1, len(df) + 1))

df['attendance_rate'] = ((30 - df['Absences']) / 30 * 100).round(2)

features = ['GPA', 'StudyTimeWeekly', 'attendance_rate']
x = df[features].copy()

print("\nSelected Features")
print(features)

print("\nMissing Values before handling:\n", x.isnull().sum())

for col in features:
    x[col] = x[col].fillna(x[col].median())

print("\nMissing Values after handling:\n", x.isnull().sum())

scaler   = StandardScaler()
X_scaled = scaler.fit_transform(x)
print("\nStandard Scaling applied to all selected features.")

wcss_list = []  

for i in range(2, 7):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss_list.append(kmeans.inertia_)

mtp.plot(range(2, 7), wcss_list)
mtp.title('The Elbow Method Graph')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

for k, wcss in zip(range(2, 7), wcss_list):
    print(f"  K={k} -> WCSS: {wcss:.2f}")

print("\nOptimal K selected: 3")

kmeans    = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(X_scaled)
df['Cluster'] = y_predict

x_raw = x.values
mtp.scatter(x_raw[y_predict == 0, 1], x_raw[y_predict == 0, 0], s=100, c='blue',  label='Cluster 1')  #for first cluster
mtp.scatter(x_raw[y_predict == 1, 1], x_raw[y_predict == 1, 0], s=100, c='green', label='Cluster 2')  #for second cluster
mtp.scatter(x_raw[y_predict == 2, 1], x_raw[y_predict == 2, 0], s=100, c='red',   label='Cluster 3')  #for third cluster
mtp.scatter(
    scaler.inverse_transform(kmeans.cluster_centers_)[:, 1],
    scaler.inverse_transform(kmeans.cluster_centers_)[:, 0],
    s=300, c='yellow', label='Centroid'
)
mtp.title('Student Academic Clusters (K-Means)')
mtp.xlabel('Study Hours (Weekly)')
mtp.ylabel('GPA')
mtp.legend()
mtp.show()

print("\nFinal Dataset: Student IDs with Assigned Clusters")
print(df[['StudentID', 'GPA', 'StudyTimeWeekly',
          'attendance_rate', 'Cluster']].head(20).to_string())

print("\nCluster Summary")
print(df.groupby('Cluster')[features].mean().round(2).to_string())
