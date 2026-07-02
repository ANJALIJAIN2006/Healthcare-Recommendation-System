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

# ---------------------------------------
# Load Model
# ---------------------------------------

model = joblib.load(BASE_DIR / "models" / "disease_model.pkl")
encoder = joblib.load(BASE_DIR / "models" / "label_encoder.pkl")

medicine_df = pd.read_csv(BASE_DIR / "data" / "raw" / "medicine.csv")
lifestyle_df = pd.read_csv(BASE_DIR / "data" / "raw" / "lifestyle.csv")

st.set_page_config(
    page_title="Recommendation",
    layout="wide"
)

st.title("Healthcare Recommendations")

st.write("Personalized recommendations based on the predicted disease.")

st.divider()

# ---------------------------------------
# Check Patient Data
# ---------------------------------------

if "patient" not in st.session_state:
    st.warning("Please complete the Patient Registration page first.")
    st.stop()

patient = st.session_state["patient"]

# ---------------------------------------
# Prediction
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

prediction = model.predict(pd.DataFrame([patient_input]))
disease = encoder.inverse_transform(prediction)[0]

st.subheader("Predicted Disease")

st.success(disease)

st.divider()

# ---------------------------------------
# Medicine
# ---------------------------------------

st.subheader("Medicine Recommendation")

medicine = medicine_df[
    medicine_df["disease"] == disease
]

if not medicine.empty:

    st.table(medicine)

else:

    st.info("No medicine recommendation available.")

st.divider()

# ---------------------------------------
# Lifestyle
# ---------------------------------------

st.subheader("Lifestyle Recommendation")

life = lifestyle_df[
    lifestyle_df["disease"] == disease
]

if not life.empty:

    row = life.iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Diet")
        st.write(row["diet"])

        st.write("### Water Intake")
        st.write(row["water"])

    with col2:
        st.write("### Exercise")
        st.write(row["exercise"])

        st.write("### Sleep")
        st.write(row["sleep"])

    st.divider()

    st.subheader("Precautions")

    st.write(row["precautions"])

else:

    st.info("No lifestyle recommendation available.")

st.divider()

# ---------------------------------------
# Doctor Advice
# ---------------------------------------

st.subheader("Doctor Advice")

st.info("""
This recommendation is generated using a machine learning model.

It is intended for educational purposes only and should not replace professional medical advice.

If symptoms are severe or persist, consult a qualified healthcare professional immediately.
""")
st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("← Prediction", use_container_width=True):
        st.switch_page("pages/2Prediction.py")

with col2:
    if st.button("Next → Analytics", use_container_width=True):
        st.switch_page("pages/4_Analytics.py")