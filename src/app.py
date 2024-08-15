import streamlit as st
import pandas as pd
import numpy as np
import requests
import os

# os.system("python3 -m uvicorn inference:app --reload")


st.header("Enter new feature values")

# with st.container("Entry Data"):
    

with st.container():
    

    # Input fields for 9 features
    feature1 = st.text_input("Feature 1")
    feature2 = st.text_input("Feature 2")
    feature3 = st.text_input("Feature 3")
    feature4 = st.text_input("Feature 4")
    feature5 = st.text_input("Feature 5")
    feature6 = st.text_input("Feature 6")
    feature7 = st.text_input("Feature 7")
    feature8 = st.text_input("Feature 8")
    feature9 = st.text_input("Feature 9")
    feature10 = st.text_input("Feature 10")

    button = st.button("Predict")


if button:
    data = {
        "feature_0" : float(feature1),
        "feature_1" : float(feature2),
        "feature_2" : float(feature3),
        "feature_3" : float(feature4),
        "feature_4" : float(feature5),
        "feature_5" : float(feature6),
        "feature_6" : float(feature7),
        "feature_7" : float(feature8),
        "feature_8" : float(feature9),
        "feature_9" : float(feature10),
        

    }




    url = "http://127.0.0.1:8000/predict"
    response = requests.post(url, json=data)

    response_data = response.json()

    print(response_data)

    st.write(f"The predicted value for the input features provided is {response_data['prediction']}")