import pandas as pd
import joblib
from bmi import calculate_bmi, bmi_category
from risk import health_risk
# Load model
model = joblib.load("models/disease_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")

# Load datasets
medicine_df = pd.read_csv("data/raw/medicine.csv")
lifestyle_df = pd.read_csv("data/raw/lifestyle.csv")

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
    "age":25,

    "height":170,
    "weight":68
}

# Convert to DataFrame
# Calculate BMI
bmi = calculate_bmi(patient["weight"], patient["height"])
category = bmi_category(bmi)

# Create a copy for the ML model
model_input = patient.copy()

# Remove fields that were NOT used for training
model_input.pop("height")
model_input.pop("weight")

# Convert to DataFrame
patient_df = pd.DataFrame([model_input])

# Predict disease
prediction = model.predict(patient_df)
disease = encoder.inverse_transform(prediction)[0]

print("="*50)
print("HEALTHCARE RECOMMENDATION SYSTEM")
print("="*50)

print("\nPredicted Disease:", disease)
print("\nBMI")
print("BMI Value :", bmi)
print("Category  :", category)
# Count symptoms
symptom_count = (
    patient["fever"] +
    patient["cough"] +
    patient["headache"] +
    patient["fatigue"] +
    patient["body_pain"] +
    patient["sore_throat"] +
    patient["nausea"] +
    patient["vomiting"] +
    patient["diarrhea"]
)
risk = health_risk(
    bmi,
    patient["age"],
    symptom_count
)

print("\nHealth Risk :", risk)
print("\nDoctor Advice")

if risk == "High":
    print("Visit a doctor immediately.")

elif risk == "Medium":
    print("Consult a doctor within 24 hours.")

else:
    print("Home care may be enough. Monitor your symptoms and consult a doctor if they worsen.")

# Confidence
confidence = model.predict_proba(patient_df).max() * 100
print(f"Confidence: {confidence:.2f}%")

# Medicine Recommendation
medicine = medicine_df[medicine_df["disease"] == disease]

if not medicine.empty:
    print("\n💊 Medicine Recommendation")
    print("Medicine :", medicine.iloc[0]["medicine"])
    print("Dosage   :", medicine.iloc[0]["dosage"])
else:
    print("\nNo medicine recommendation found.")

# Lifestyle Recommendation
lifestyle = lifestyle_df[lifestyle_df["disease"] == disease]

if not lifestyle.empty:
    print("\n🥗 Lifestyle Recommendation")
    print("Diet        :", lifestyle.iloc[0]["diet"])
    print("Exercise    :", lifestyle.iloc[0]["exercise"])
    print("Water Intake:", lifestyle.iloc[0]["water"])
else:
    print("\nNo lifestyle recommendation found.")

print("\n" + "="*50)
print("⚠️ DISCLAIMER")
print("="*50)
print("This system is for educational purposes only.")
print("Always consult a qualified healthcare professional before taking any medicine.")