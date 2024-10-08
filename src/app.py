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
    feature1 = st.text_input("Nitrogen")
    feature2 = st.text_input("Phosphorous")
    feature3 = st.text_input("Potassium")
    feature4 = st.text_input("Temperature")
    feature5 = st.text_input("Humidity")
    feature6 = st.text_input("pH")
    feature7 = st.text_input("Rainfall")
    
    button = st.button("Predict")


if button:
    data = {
        "feature_0" : float(feature1),
        "feature_1" : float(feature2),
        "feature_2" : float(feature3),
        "feature_3" : float(feature4),
        "feature_4" : float(feature5),
        "feature_5" : float(feature6),
        "feature_6" : float(feature7)

    }




    url = "https://aml-inference-backend.azurewebsites.net/predict"
    response = requests.post(url, json=data)

    response_data = response.json()

    print(response_data)

    st.write(f"The predicted crop for the input features provided is {response_data['prediction']}")
