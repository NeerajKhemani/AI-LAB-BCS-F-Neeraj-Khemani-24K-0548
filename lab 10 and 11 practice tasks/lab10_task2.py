import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('spam.csv', encoding='latin-1')
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

print(df.head())
print(f"\nDataset Shape: {df.shape}")
print("\nClass Distribution:")
print(df['label'].value_counts())

df['label_encoded'] = (df['label'] == 'spam').astype(int)

df['word_count']     = df['message'].apply(lambda x: len(x.split()))
df['char_count']     = df['message'].apply(lambda x: len(x))
df['has_hyperlink']  = df['message'].apply(lambda x: int('http' in x.lower()))
df['has_free']       = df['message'].apply(lambda x: int('free' in x.lower()))
df['has_win']        = df['message'].apply(lambda x: int('win' in x.lower()))
df['has_urgent']     = df['message'].apply(lambda x: int('urgent' in x.lower()))
df['exclaim_count']  = df['message'].apply(lambda x: x.count('!'))
df['digit_count']    = df['message'].apply(lambda x: sum(c.isdigit() for c in x))
df['upper_count']    = df['message'].apply(lambda x: sum(c.isupper() for c in x))

print("\nMissing Values:\n", df.isnull().sum())

x = df[['word_count', 'char_count', 'has_hyperlink', 'has_free',
         'has_win', 'has_urgent', 'exclaim_count',
         'digit_count', 'upper_count']].values
y = df['label_encoded'].values

scaler   = StandardScaler()
x_scaled = scaler.fit_transform(x)
print("\nFeature scaling applied using StandardScaler.")

X_train, X_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=42)
print(f"\nTrain size: {len(X_train)}, Test size: {len(X_test)}")

svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

print("\nSVM Accuracy:", accuracy_score(y_test, y_pred))

print('\nSVM Testing Accuracy')
testingAccSVM = accuracy_score(y_test, y_pred) * 100
print(f"Testing Accuracy: {testingAccSVM:.2f}%")

new_email = pd.DataFrame({
    'word_count':    [20],
    'char_count':    [120],
    'has_hyperlink': [1],
    'has_free':      [1],
    'has_win':       [1],
    'has_urgent':    [1],
    'exclaim_count': [3],
    'digit_count':   [5],
    'upper_count':   [10]
})

new_email_scaled = scaler.transform(new_email)
email_prediction = svm.predict(new_email_scaled)

print('\nNew Email Classification')
print("Email classified as:", "SPAM" if email_prediction[0] == 1 else "NOT SPAM")
