import pandas as pd
import joblib

# Load model
model = joblib.load("models/disease_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")

# Sample patient
patient = {
    "fever":1,
    "cough":1,
    "headache":1,
    "fatigue":1,
    "body_pain":1,
    "sore_throat":1,
    "nausea":0,
    "vomiting":0,
    "diarrhea":0,
    "age":25
}

# Convert to DataFrame
patient_df = pd.DataFrame([patient])

# Predict disease
prediction = model.predict(patient_df)

# Decode prediction
disease = encoder.inverse_transform(prediction)

print("Predicted Disease:", disease[0])

# Confidence
probability = model.predict_proba(patient_df)

confidence = probability.max()*100

print(f"Confidence: {confidence:.2f}%")