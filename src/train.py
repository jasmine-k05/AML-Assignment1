from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

# Splitting the dataset into training and testing sets

df = pd.read_csv("../data/dummy_data.csv")

df['target'] = df['target'].astype('category')

X = df[[i for i in df.columns if i != 'target']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Random Forest Classifier
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Training the model
rf_clf.fit(X_train, y_train)

# Making predictions
y_pred = rf_clf.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

with open("../models/random_forest_model.pkl","wb") as output_model:
    pickle.dump(rf_clf, output_model)
    
