import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv('Housing.csv')
print(df.head())
print(f"\nDataset Shape: {df.shape}")

print("\nMissing Values:\n", df.isnull().sum())
# no missing values

binary_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
for col in binary_cols:
    df[col] = (df[col] == 'yes').astype(int)

le = LabelEncoder()
df['furnishingstatus'] = le.fit_transform(df['furnishingstatus'])

print("\nEncoded furnishingstatus:",
      dict(zip(le.classes_, le.transform(le.classes_))))
print("\nDataset after encoding:\n", df.head())

x = df.drop('price', axis=1).values
y = df['price'].values

scaler   = StandardScaler()
x_scaled = scaler.fit_transform(x)
print("\nFeature scaling applied using StandardScaler.")

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=42)
print(f"\nTrain size: {len(x_train)}, Test size: {len(x_test)}")

LR      = LinearRegression()
ModelLR = LR.fit(x_train, y_train)
PredictionLR = ModelLR.predict(x_test)

print("\nPredictions:", PredictionLR[:5])

print('\nLR Testing Accuracy')
teachLR      = r2_score(y_test, PredictionLR)
testingAccLR = teachLR * 100
mae_lr       = mean_absolute_error(y_test, PredictionLR)
rmse_lr      = np.sqrt(mean_squared_error(y_test, PredictionLR))
print(f"MAE        : {mae_lr:,.2f}")
print(f"RMSE       : {rmse_lr:,.2f}")
print(f"R2 Score   : {testingAccLR:.2f}%")


DT      = DecisionTreeRegressor(random_state=42)
ModelDT = DT.fit(x_train, y_train)
PredictionDT = DT.predict(x_test)
print("\nPredictions:", PredictionDT[:5])

print('DT Training Accuracy')
tracDT        = DT.score(x_train, y_train)
TrainingAccDT = tracDT * 100
print(f"Training Accuracy: {TrainingAccDT:.2f}%")

print('DT Testing Accuracy')
mae_dt        = mean_absolute_error(y_test, PredictionDT)
rmse_dt       = np.sqrt(mean_squared_error(y_test, PredictionDT))
teacDT        = r2_score(y_test, PredictionDT)
testingAccDT  = teacDT * 100
print(f"MAE        : {mae_dt:,.2f}")
print(f"RMSE       : {rmse_dt:,.2f}")
print(f"Testing Accuracy (R2): {testingAccDT:.2f}%")

print("\nPredicted vs Actual")
comparison = pd.DataFrame({
    'Actual':       y_test[:10],
    'LR Predicted': PredictionLR[:10].round(0),
    'DT Predicted': PredictionDT[:10].round(0)
})
print(comparison.to_string())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_test, PredictionLR, s=50, c='steelblue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()], 'r--', lw=2)
plt.title('Predicted vs Actual – Linear Regression')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')

plt.subplot(1, 2, 2)
plt.scatter(y_test, PredictionDT, s=50, c='darkorange', alpha=0.6)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()], 'r--', lw=2)
plt.title('Predicted vs Actual – Decision Tree')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')

plt.tight_layout()
plt.show()


print("\nMetric     Linear Regression    Decision Tree")
print("-----------------------------------------------")
for m, lr, dt in zip(['MAE', 'RMSE', 'R2 (%)'],
                     [mae_lr,  rmse_lr,  testingAccLR],
                     [mae_dt,  rmse_dt,  testingAccDT]):
    print(f"{m:<10} {lr:>16,.2f}    {dt:>12,.2f}")

best = "Linear Regression" if testingAccLR >= testingAccDT else "Decision Tree"
print(f"\nBEST MODEL: {best}")
print("  - Linear Regression captures linear relationships with lower overfitting.")
print("  - Decision Tree achieves 100% training accuracy but overfits on test data.")
print("  - Linear Regression gives more reliable generalisation on unseen data.")
