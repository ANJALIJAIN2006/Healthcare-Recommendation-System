import streamlit as st
import pandas as pd
import joblib
import sys
from pathlib import Path

# ---------------------------------------
# Project Path
# ---------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR / "src"))

from bmi import calculate_bmi, bmi_category
from risk import health_risk

# ---------------------------------------
# Load Model
# ---------------------------------------

model = joblib.load(BASE_DIR / "models" / "disease_model.pkl")
encoder = joblib.load(BASE_DIR / "models" / "label_encoder.pkl")

st.set_page_config(
    page_title="Disease Prediction",
    layout="wide"
)

st.title("Disease Prediction Dashboard")
st.write("View the predicted disease and health assessment.")
st.divider()

# ---------------------------------------
# Check Patient Data
# ---------------------------------------

if "patient" not in st.session_state:
    st.warning("Please complete the Patient Registration page first.")
    st.stop()

patient = st.session_state["patient"]

# ---------------------------------------
# Prepare Model Input
# ---------------------------------------

patient_input = {
    "fever": int(patient["fever"]),
    "cough": int(patient["cough"]),
    "headache": int(patient["headache"]),
    "fatigue": int(patient["fatigue"]),
    "body_pain": int(patient["body_pain"]),
    "sore_throat": int(patient["sore_throat"]),
    "nausea": int(patient["nausea"]),
    "vomiting": int(patient["vomiting"]),
    "diarrhea": int(patient["diarrhea"]),
    "age": patient["age"]
}

patient_df = pd.DataFrame([patient_input])

# ---------------------------------------
# Prediction
# ---------------------------------------

prediction = model.predict(patient_df)
disease = encoder.inverse_transform(prediction)[0]

confidence = model.predict_proba(patient_df).max() * 100

# ---------------------------------------
# BMI
# ---------------------------------------

bmi = calculate_bmi(
    patient["weight"],
    patient["height"]
)

bmi_status = bmi_category(bmi)

# ---------------------------------------
# Health Risk
# ---------------------------------------

symptom_count = sum([
    patient["fever"],
    patient["cough"],
    patient["headache"],
    patient["fatigue"],
    patient["body_pain"],
    patient["sore_throat"],
    patient["nausea"],
    patient["vomiting"],
    patient["diarrhea"]
])

risk = health_risk(
    bmi,
    patient["age"],
    symptom_count
)

# ---------------------------------------
# Save Prediction History
# ---------------------------------------

history_folder = BASE_DIR / "history"
history_folder.mkdir(exist_ok=True)

history_path = history_folder / "history.csv"
st.write("History Path:", history_path)

new_record = pd.DataFrame([{
    "Name": patient["name"],
    "Age": patient["age"],
    "Gender": patient["gender"],
    "Disease": disease,
    "Confidence": round(confidence, 2),
    "BMI": round(bmi, 2)
}])


current_record = (
    patient["name"],
    disease,
    round(confidence, 2)
)

if st.session_state.get("last_saved_prediction") != current_record:

    if history_path.exists():

        new_record.to_csv(
            history_path,
            mode="a",
            header=False,
            index=False
        )

    else:

        new_record.to_csv(
            history_path,
            index=False
        )

    st.session_state["last_saved_prediction"] = current_record

# ---------------------------------------
# Dashboard Metrics
# ---------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Predicted Disease", disease)
col2.metric("Confidence", f"{confidence:.2f}%")
col3.metric("BMI", round(bmi, 2))
col4.metric("Health Risk", risk)

st.divider()

# ---------------------------------------
# Confidence
# ---------------------------------------

st.subheader("Prediction Confidence")

st.progress(int(confidence))

st.write(f"Model Confidence: **{confidence:.2f}%**")

st.divider()

# ---------------------------------------
# Patient Summary
# ---------------------------------------

st.subheader("Patient Summary")

left, right = st.columns(2)

with left:
    st.write(f"**Name:** {patient['name']}")
    st.write(f"**Age:** {patient['age']}")
    st.write(f"**Gender:** {patient['gender']}")

with right:
    st.write(f"**Height:** {patient['height']} cm")
    st.write(f"**Weight:** {patient['weight']} kg")
    st.write(f"**Blood Group:** {patient['blood']}")

st.divider()

# ---------------------------------------
# BMI Assessment
# ---------------------------------------

st.subheader("BMI Assessment")

col1, col2 = st.columns(2)

col1.metric("BMI Value", round(bmi, 2))
col2.metric("Category", bmi_status)

st.divider()

# ---------------------------------------
# Selected Symptoms
# ---------------------------------------

st.subheader("Selected Symptoms")

selected = []

symptoms = [
    "fever",
    "cough",
    "headache",
    "fatigue",
    "body_pain",
    "sore_throat",
    "nausea",
    "vomiting",
    "diarrhea"
]

for symptom in symptoms:
    if patient[symptom]:
        selected.append(symptom.replace("_", " ").title())

if selected:
    st.write(", ".join(selected))
else:
    st.info("No symptoms selected.")

st.divider()

# ---------------------------------------
# Prediction Summary
# ---------------------------------------

st.subheader("Prediction Summary")

summary = pd.DataFrame({
    "Field": [
        "Patient Name",
        "Predicted Disease",
        "Confidence",
        "BMI",
        "BMI Category",
        "Health Risk"
    ],
    "Value": [
        patient["name"],
        disease,
        f"{confidence:.2f}%",
        round(bmi, 2),
        bmi_status,
        risk
    ]
})

st.dataframe(
    summary,
    hide_index=True,
    use_container_width=True
)
st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("← Back", use_container_width=True):
        st.switch_page("pages/1_Home.py")

with col2:
    if st.button("Next → Recommendation", use_container_width=True):
        st.switch_page("pages/3_Recommendation.py")