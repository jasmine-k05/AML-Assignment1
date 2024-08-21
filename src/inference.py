from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import logging
import uvicorn

# Load the model from the pickle file
with open('../models/random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize FastAPI
app = FastAPI()

# Define the input data schema
class InputData(BaseModel):
    feature_0: float
    feature_1: float
    feature_2: float
    feature_3: float
    feature_4: float
    feature_5: float
    feature_6: float
    
# Define the prediction endpoint
@app.post("/predict")
async def predict(data: InputData):


    # Convert input data to a numpy array
    input_features = np.array([[data.feature_0, data.feature_1, data.feature_2, data.feature_3, data.feature_4,
                                data.feature_5, data.feature_6]])


    print(input_features)
    # Make prediction
    prediction = model.predict(input_features)

    print(prediction)
    
    # Return the prediction result
    return {"prediction": int(prediction[0])}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')