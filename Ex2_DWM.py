import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'C:\Users\LENOVO\Downloads/data.csv')

o = pd.get_dummies(df['category'])
le = LabelEncoder()
l = le.fit_transform (df['category'])
print("\nOriginal data:\n",df)
print("\nOne-hot encoded data:\n",o)
print("\nLabel encoded data:\n",l)

ss = StandardScaler()
s = ss.fit_transform(df[['feature1']])
mms = MinMaxScaler()
m = mms.fit_transform (df[['feature1']])
print("\nStandardized data:\n",s)
print("\nMin-Max scaled data:\n",m)

X = df[['feature1', 'feature2']].values
y = df['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training data:")
print("X_train:", X_train)
print("y_train:", y_train)
print("\nTesting data:")
print("X_test:", X_test)
print("y_test:", y_test)
