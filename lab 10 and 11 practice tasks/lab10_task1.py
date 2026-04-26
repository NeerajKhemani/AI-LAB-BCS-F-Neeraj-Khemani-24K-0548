import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('Housing.csv')
print(df.head())
print(f"\nShape: {df.shape}")


print("\nMissing Values:\n", df.isnull().sum())

binary_cols = ['mainroad', 'guestroom', 'basement','hotwaterheating', 'airconditioning', 'prefarea']

for col in binary_cols:
    df[col] = (df[col] == 'yes').astype(int)

le = LabelEncoder()
df['furnishingstatus'] = le.fit_transform(df['furnishingstatus'])

print("\nEncoded furnishingstatus:", dict(zip(le.classes_, le.transform(le.classes_))))
print("\nDataset after encoding:\n", df.head())

x = df.drop('price', axis=1).values
y = df['price'].values

print("\nFeatures used:", df.drop('price', axis=1).columns.tolist())

scaler   = StandardScaler()
x_scaled = scaler.fit_transform(x)
print("Feature scaling applied using StandardScaler.")

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=42)
print(f"\nTrain size: {len(x_train)}, Test size: {len(x_test)}")

LR      = LinearRegression()
ModelLR = LR.fit(x_train, y_train)

PredictionLR = ModelLR.predict(x_test)

print("\nPredictions:", PredictionLR[:5])

print('\nLR Testing Accuracy')
teachLR      = r2_score(y_test, PredictionLR)
testingAccLR = teachLR * 100
print(f"R2 Score (Testing Accuracy): {testingAccLR:.2f}%")

rmse = np.sqrt(mean_squared_error(y_test, PredictionLR))
print(f"Root Mean Squared Error (RMSE): {rmse:,.2f}")

new_house = pd.DataFrame([{
    'area':             5000,
    'bedrooms':         3,
    'bathrooms':        2,
    'stories':          2,
    'mainroad':         1,
    'guestroom':        0,
    'basement':         1,
    'hotwaterheating':  0,
    'airconditioning':  1,
    'parking':          1,
    'prefarea':         0,
    'furnishingstatus': 1   
}])

new_house_scaled = scaler.transform(new_house)
predicted_price  = ModelLR.predict(new_house_scaled)

print('\n New House Prediction')
print(f"Predicted House Price: {predicted_price[0]:,.2f}")