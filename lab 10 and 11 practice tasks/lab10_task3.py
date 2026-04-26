import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv('marketing_campaign.csv', sep=';')

print(df.head())
print(f"\nDataset Shape: {df.shape}")

print("\nMissing Values:\n", df.isnull().sum())
df = df.dropna(subset=['Income'])
print(f"\nDataset size after dropping missing rows: {len(df)}")


df['TotalSpending'] = (df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds'])

median_spending = df['TotalSpending'].median()
df['label'] = (df['TotalSpending'] > median_spending).astype(int)

print(f"\nMedian Spending: {median_spending:.2f}")
print("Class Distribution:\n", df['label'].value_counts())

features = ['Income', 'Recency', 'NumDealsPurchases', 'NumWebPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 'TotalSpending']

x = df[features].copy()
y = df['label'].values

Q1  = x['Income'].quantile(0.25)
Q3  = x['Income'].quantile(0.75)
IQR = Q3 - Q1
x   = x[(x['Income'] >= Q1 - 1.5 * IQR) &
         (x['Income'] <= Q3 + 1.5 * IQR)]
y   = df.loc[x.index, 'label'].values
x   = x.values

print(f"\nDataset size after outlier removal: {len(x)}")

scaler   = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)
print(f"Training samples: {len(x_train)}, Testing samples: {len(x_test)}")


svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(x_train, y_train)

y_pred_svm = svm.predict(x_test)
print("\nSVM Predictions (sample):", y_pred_svm[:10])

print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
testingAccSVM = accuracy_score(y_test, y_pred_svm) * 100
print(f"Testing Accuracy: {testingAccSVM:.2f}%")


DT = DecisionTreeClassifier()


ModelDT = DT.fit(x_train, y_train)
PredictionDT = DT.predict(x_test)
print("\nPredictions:", PredictionDT[:10])

print('DT Training Accuracy')
tracDT        = DT.score(x_train, y_train)
TrainingAccDT = tracDT * 100
print(f"Training Accuracy: {TrainingAccDT:.2f}%")

print('DT Testing Accuracy')
teacDT        = accuracy_score(y_test, PredictionDT)
testingAccDT  = teacDT * 100
print(f"Testing Accuracy: {testingAccDT:.2f}%")

new_customer = pd.DataFrame({
    'Income':             [75000],
    'Recency':            [20],
    'NumDealsPurchases':  [3],
    'NumWebPurchases':    [8],
    'NumStorePurchases':  [6],
    'NumWebVisitsMonth':  [4],
    'TotalSpending':      [1200]
})

new_customer_scaled      = scaler.transform(new_customer)
svm_result               = svm.predict(new_customer_scaled)
dt_result                = DT.predict(new_customer_scaled)

print('\nNew Customer Classification')
print("SVM Classification        :", "High-Value" if svm_result[0] == 1 else "Low-Value")
print("Decision Tree Classification:", "High-Value" if dt_result[0] == 1 else "Low-Value")
