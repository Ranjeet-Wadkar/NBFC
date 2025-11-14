from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Load model and feature list
model = joblib.load("credit_score_model.pkl")
features = joblib.load("model_features.pkl")

app = FastAPI(title="Credit Score Prediction API")

# Add CORS middleware to allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def home():
    return {"message": "Credit Score Prediction API is running!"}

# Define input schema
class CustomerData(BaseModel):
    data: dict  # key-value pairs of feature: value

@app.post("/predict")
def predict_credit_score(customer: CustomerData):
    df = pd.DataFrame([customer.data])

    for col in features:
        if col not in df.columns:
            df[col] = 0

    df = df[features]

    prob_good = 1 - model.predict_proba(df)[0][1]
    credit_score = prob_good * 900

    coef = model.coef_[0]
    intercept = model.intercept_[0]
    contrib = df.values[0] * coef
    scale_factor = credit_score / (intercept + contrib.sum())
    contrib_scaled = contrib * scale_factor

    reasoning = []
    for f, val, c in zip(features, df.values[0], contrib_scaled):
        direction = "increase" if c > 0 else "decrease"
        reasoning.append({
            "feature": f,
            "value": float(val),
            "contribution": float(round(c, 3)),
            "effect": direction
        })

    return {
        "credit_score": round(float(credit_score), 2),
        "reasoning": reasoning
}