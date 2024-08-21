# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, PowerTransformer, LabelEncoder, MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.feature_selection import mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report  # Import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Ridge, Lasso


# Load dataset from Google Drive
file_path = "../data/Crop_recommendation (1).csv"
df = pd.read_csv(file_path)

# Display the first 2 rows
print(df.head(2))

# Visualize class distribution
plt.figure(figsize=(12, 8))
sns.countplot(y=df['label'], order=df['label'].value_counts().index)
plt.title('Class Distribution of Crops', fontsize=16)
plt.xlabel('Number of Samples', fontsize=14)
plt.ylabel('Crop', fontsize=14)
plt.show()

# Data Preprocessing
X = df.drop('label', axis=1)
y = df['label']

# Encode labels
le = LabelEncoder()
y = le.fit_transform(y)

# Handle imbalanced data using SMOTE
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)  # Now recognized

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)

# Plot the confusion matrix
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Save the model for future use (optional)
import pickle
with open('../models/random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)

