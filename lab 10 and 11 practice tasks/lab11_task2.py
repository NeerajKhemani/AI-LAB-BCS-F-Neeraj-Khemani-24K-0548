import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage':           [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency':   [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost':  [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type':      ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)
print(df.head(10))

le = LabelEncoder()
df['vehicle_type_encoded'] = le.fit_transform(df['vehicle_type'])
print("\nVehicle Type Encoding:", dict(zip(le.classes_, le.transform(le.classes_))))

x = df[['mileage', 'fuel_efficiency', 'maintenance_cost', 'vehicle_type_encoded']].values

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

kmeans_no_scale    = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_predict_no_scale = kmeans_no_scale.fit_predict(x)

mtp.scatter(x[y_predict_no_scale == 0, 0], x[y_predict_no_scale == 0, 1], s=100, c='blue',  label='Cluster 1')  #for first cluster
mtp.scatter(x[y_predict_no_scale == 1, 0], x[y_predict_no_scale == 1, 1], s=100, c='green', label='Cluster 2')  #for second cluster
mtp.scatter(x[y_predict_no_scale == 2, 0], x[y_predict_no_scale == 2, 1], s=100, c='red',   label='Cluster 3')  #for third cluster
mtp.scatter(kmeans_no_scale.cluster_centers_[:, 0], kmeans_no_scale.cluster_centers_[:, 1], s=300, c='yellow', label='Centroid')
mtp.title('Vehicle Clusters (Without Scaling)')
mtp.xlabel('Mileage')
mtp.ylabel('Fuel Efficiency')
mtp.legend()
mtp.show()

df['Cluster_NoScale'] = y_predict_no_scale
print("Clusters (without scaling):")
print(df[['vehicle_serial_no', 'vehicle_type', 'Cluster_NoScale']])

print("\nCLUSTERING WITH SCALING (except vehicle_type)")

x_to_scale = df[['mileage', 'fuel_efficiency', 'maintenance_cost']].values
x_cat      = df[['vehicle_type_encoded']].values

scaler    = StandardScaler()
X_scaled  = scaler.fit_transform(x_to_scale)
X_combined = nm.hstack([X_scaled, x_cat])

wcss_list = [] 

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_combined)
    wcss_list.append(kmeans.inertia_)

mtp.plot(range(1, 11), wcss_list)
mtp.title('The Elbow Method Graph (With Scaling)')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

kmeans_scaled    = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_predict_scaled = kmeans_scaled.fit_predict(X_combined)

mtp.scatter(x[y_predict_scaled == 0, 0], x[y_predict_scaled == 0, 1], s=100, c='blue',  label='Cluster 1')  #for first cluster
mtp.scatter(x[y_predict_scaled == 1, 0], x[y_predict_scaled == 1, 1], s=100, c='green', label='Cluster 2')  #for second cluster
mtp.scatter(x[y_predict_scaled == 2, 0], x[y_predict_scaled == 2, 1], s=100, c='red',   label='Cluster 3')  #for third cluster
mtp.scatter(kmeans_scaled.cluster_centers_[:, 0], kmeans_scaled.cluster_centers_[:, 1], s=300, c='yellow', label='Centroid')
mtp.title('Vehicle Clusters (With Scaling)')
mtp.xlabel('Mileage')
mtp.ylabel('Fuel Efficiency')
mtp.legend()
mtp.show()

df['Cluster_Scaled'] = y_predict_scaled
print("Clusters (with scaling):")
print(df[['vehicle_serial_no', 'vehicle_type', 'Cluster_NoScale', 'Cluster_Scaled']])



## comparison:
##  WITHOUT Scaling:
##  - Mileage (75,000-300,000) completely dominates clustering.
##  - fuel_efficiency and vehicle_type are nearly ignored.
##  - Clusters are essentially just groupings by mileage alone.

##   WITH Scaling (except vehicle_type):
##  - Mileage, fuel_efficiency, maintenance_cost all contribute equally.
##    - Clusters reflect true usage patterns across all features.
##  - More meaningful groups: Trucks vs Sedans vs Hatchbacks by actual usage.

## Scaling is essential when features have very different ranges.
