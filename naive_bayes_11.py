# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset
dataset = pd.read_csv('Social_Network_Ads.csv')

# Selecting features (Age, EstimatedSalary) and target variable (Purchased)
X = dataset.iloc[:, [2, 3]].values  # Features
y = dataset.iloc[:, -1].values      # Target

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the Naïve Bayes model
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting test results
y_pred = classifier.predict(X_test)

# Evaluating model performance
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Printing results
print("Confusion Matrix:")
print(cm)
print("\nAccuracy Score:", accuracy)
