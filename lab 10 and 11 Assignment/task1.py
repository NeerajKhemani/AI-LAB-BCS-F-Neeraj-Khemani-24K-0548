import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay)
import matplotlib.pyplot as plt

df = pd.read_csv('creditcard.csv')
print(df.head())
print(f"\nDataset Shape: {df.shape}")
print("\nClass Distribution (before handling imbalance):")
print(df['Class'].value_counts())
print(f"\nFraud percentage: {df['Class'].mean()*100:.4f}%")

fraud       = df[df['Class'] == 1]
legit       = df[df['Class'] == 0].sample(n=len(fraud), random_state=42)
df_balanced = pd.concat([fraud, legit]).sample(frac=1, random_state=42)

print(df_balanced['Class'].value_counts())
print(f"Balanced dataset size: {len(df_balanced)}")

x = df_balanced.drop('Class', axis=1).values
y = df_balanced['Class'].values

scaler   = StandardScaler()
x_scaled = scaler.fit_transform(x)
print("\nFeature scaling applied using StandardScaler.")

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=42)
print(f"\nTrain size: {len(x_train)}, Test size: {len(x_test)}")

LR      = LogisticRegression(max_iter=1000)
ModelLR = LR.fit(x_train, y_train)
PredictionLR = ModelLR.predict(x_test)

print('\nLR Testing Accuracy')
print(f"Accuracy  : {accuracy_score(y_test,  PredictionLR)*100:.2f}%")
print(f"Precision : {precision_score(y_test, PredictionLR)*100:.2f}%")
print(f"Recall    : {recall_score(y_test,    PredictionLR)*100:.2f}%")
print(f"F1-Score  : {f1_score(y_test,        PredictionLR)*100:.2f}%")

cm_lr = confusion_matrix(y_test, PredictionLR)
disp  = ConfusionMatrixDisplay(confusion_matrix=cm_lr, display_labels=['Legit', 'Fraud'])
fig, ax = plt.subplots(figsize=(5, 4))
disp.plot(ax=ax, colorbar=False)
plt.title('Confusion Matrix - Logistic Regression')
plt.tight_layout()
print("\n")
plt.show()

RF      = RandomForestClassifier(n_estimators=50, random_state=42)
ModelRF = RF.fit(x_train, y_train)
PredictionRF = ModelRF.predict(x_test)

print('\nRF Testing Accuracy')
print(f"Accuracy  : {accuracy_score(y_test,  PredictionRF)*100:.2f}%")
print(f"Precision : {precision_score(y_test, PredictionRF)*100:.2f}%")
print(f"Recall    : {recall_score(y_test,    PredictionRF)*100:.2f}%")
print(f"F1-Score  : {f1_score(y_test,        PredictionRF)*100:.2f}%")

cm_rf = confusion_matrix(y_test, PredictionRF)
disp  = ConfusionMatrixDisplay(confusion_matrix=cm_rf, display_labels=['Legit', 'Fraud'])
fig, ax = plt.subplots(figsize=(5, 4))
disp.plot(ax=ax, colorbar=False)
plt.title('Confusion Matrix - Random Forest')
plt.tight_layout()
print("\n")
plt.show()

metrics   = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
lr_scores = [accuracy_score(y_test,  PredictionLR),
             precision_score(y_test, PredictionLR),
             recall_score(y_test,    PredictionLR),
             f1_score(y_test,        PredictionLR)]
rf_scores = [accuracy_score(y_test,  PredictionRF),
             precision_score(y_test, PredictionRF),
             recall_score(y_test,    PredictionRF),
             f1_score(y_test,        PredictionRF)]

x_pos = np.arange(len(metrics))
width = 0.35

plt.figure(figsize=(9, 5))
plt.bar(x_pos - width/2, lr_scores, width, label='Logistic Regression', color='steelblue')
plt.bar(x_pos + width/2, rf_scores, width, label='Random Forest',       color='darkorange')
plt.xticks(x_pos, metrics)
plt.ylim(0, 1.1)
plt.ylabel('Score')
plt.title('Model Comparison - Credit Card Fraud Detection')
plt.legend()
plt.tight_layout()
print("\n")
plt.show()

print("\nMetric           Logistic Regression    Random Forest   ")
print("--------------------------------------------------------")
for m, lr, rf in zip(metrics, lr_scores, rf_scores):
    print(f"{m:<16} {lr*100:>18.2f}%    {rf*100:>12.2f}%")

rf_f1 = f1_score(y_test, PredictionRF)
lr_f1 = f1_score(y_test, PredictionLR)
best  = "Random Forest" if rf_f1 >= lr_f1 else "Logistic Regression"
print(f"\nBEST MODEL FOR IMBALANCED DATA: {best}")
print("  - For fraud detection, Recall and F1-Score matter most.")
print("  - Random Forest handles class imbalance better due to its ensemblenature, capturing complex non-linear fraud patterns.")
print("  - Logistic Regression is simpler and faster but less robust on highly skewed distributions.")
