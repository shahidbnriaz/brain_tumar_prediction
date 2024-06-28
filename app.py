import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

st.title("Brain Tumor Prediction App")

st.sidebar.header("Input Parameters")

def user_input_features():
    radius_mean = st.sidebar.slider('Radius Mean', 0.0, 30.0, 15.0)
    texture_mean = st.sidebar.slider('Texture Mean', 0.0, 30.0, 15.0)
    perimeter_mean = st.sidebar.slider('Perimeter Mean', 0.0, 200.0, 100.0)
    area_mean = st.sidebar.slider('Area Mean', 0.0, 2500.0, 1250.0)
    smoothness_mean = st.sidebar.slider('Smoothness Mean', 0.0, 1.0, 0.5)
    features = {
        'radius_mean': radius_mean,
        'texture_mean': texture_mean,
        'perimeter_mean': perimeter_mean,
        'area_mean': area_mean,
        'smoothness_mean': smoothness_mean
    }
    return pd.DataFrame(features, index=[0])

df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

# Load example dataset
# Replace with your actual dataset
data = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/breast_cancer.csv')
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict using the model
prediction = model.predict(df)
prediction_proba = model.predict_proba(df)

st.subheader('Prediction')
tumor_type = np.array(['Benign', 'Malignant'])
st.write(tumor_type[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)
