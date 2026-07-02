import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import sys
from pathlib import Path

# ------------------------------------
# Project Path
# ------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR / "src"))

from bmi import calculate_bmi

# ------------------------------------
# Load Model
# ------------------------------------

model = joblib.load(BASE_DIR / "models" / "disease_model.pkl")
encoder = joblib.load(BASE_DIR / "models" / "label_encoder.pkl")

st.set_page_config(
    page_title="Analytics",
    layout="wide"
)

st.title("Healthcare Analytics Dashboard")
st.caption("Patient health summary and prediction analytics.")

st.divider()

# ------------------------------------
# Check Patient
# ------------------------------------

if "patient" not in st.session_state:
    st.warning("Please register a patient first.")
    st.stop()

patient = st.session_state["patient"]

# ------------------------------------
# Prediction
# ------------------------------------

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

prediction = model.predict(patient_df)
disease = encoder.inverse_transform(prediction)[0]

confidence = model.predict_proba(patient_df).max() * 100

bmi = calculate_bmi(
    patient["weight"],
    patient["height"]
)

# ------------------------------------
# Dashboard Cards
# ------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric("Predicted Disease", disease)
col2.metric("Confidence", f"{confidence:.2f}%")
col3.metric("BMI", round(bmi, 2))

st.divider()

# ------------------------------------
# Charts
# ------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("Symptoms Overview")

    symptoms = {
        "Fever": patient["fever"],
        "Cough": patient["cough"],
        "Headache": patient["headache"],
        "Fatigue": patient["fatigue"],
        "Body Pain": patient["body_pain"],
        "Sore Throat": patient["sore_throat"],
        "Nausea": patient["nausea"],
        "Vomiting": patient["vomiting"],
        "Diarrhea": patient["diarrhea"]
    }

    selected = {k: v for k, v in symptoms.items() if v == 1}

    if selected:

        fig, ax = plt.subplots(figsize=(5,2.8))

        ax.bar(
            selected.keys(),
            selected.values(),
            width=0.5
        )

        ax.set_ylim(0,1.2)

        plt.xticks(rotation=25, fontsize=8)

        st.pyplot(fig)

    else:

        st.info("No symptoms selected.")

with right:

    st.subheader("Prediction Confidence")

    st.progress(int(confidence))

    st.metric(
        "Confidence Score",
        f"{confidence:.2f}%"
    )

st.divider()

# ------------------------------------
# BMI Assessment
# ------------------------------------

st.subheader("BMI Assessment")

if bmi < 18.5:
    bmi_status = "Underweight"
elif bmi < 25:
    bmi_status = "Normal"
elif bmi < 30:
    bmi_status = "Overweight"
else:
    bmi_status = "Obese"

c1, c2 = st.columns(2)

c1.metric("BMI Value", round(bmi,2))
c2.metric("BMI Category", bmi_status)

st.divider()

# ------------------------------------
# Patient Summary
# ------------------------------------

st.subheader("Patient Summary")

summary = pd.DataFrame({

    "Field":[
        "Patient Name",
        "Age",
        "Gender",
        "Blood Group",
        "Height (cm)",
        "Weight (kg)",
        "BMI",
        "Predicted Disease",
        "Confidence (%)"
    ],

    "Value":[
        patient["name"],
        patient["age"],
        patient["gender"],
        patient["blood"],
        patient["height"],
        patient["weight"],
        round(bmi,2),
        disease,
        round(confidence,2)
    ]

})

st.dataframe(
    summary,
    hide_index=True,
    use_container_width=True
)

st.divider()
# ------------------------------------
# Prediction History
# ------------------------------------

st.subheader("Prediction History")

history_path = BASE_DIR / "history" / "history.csv"

if history_path.exists():

    history = pd.read_csv(history_path)

    # Ensure required columns exist
    required_columns = [
        "Name",
        "Age",
        "Gender",
        "Disease",
        "Confidence",
        "BMI"
    ]

    for col in required_columns:
        if col not in history.columns:
            history[col] = None

    # Convert numeric columns safely
    history["Confidence"] = pd.to_numeric(
        history["Confidence"],
        errors="coerce"
    )

    history["BMI"] = pd.to_numeric(
        history["BMI"],
        errors="coerce"
    )

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ------------------------------------
    # Project Statistics
    # ------------------------------------

    st.subheader("Project Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Predictions",
        len(history)
    )

    c2.metric(
        "Unique Diseases",
        history["Disease"].nunique()
    )

    avg_bmi = history["BMI"].mean()

    if pd.isna(avg_bmi):
        avg_bmi = 0

    c3.metric(
        "Average BMI",
        f"{avg_bmi:.2f}"
    )

    st.divider()

    # ------------------------------------
    # Disease Distribution
    # ------------------------------------

    st.subheader("Disease Distribution")

    disease_counts = history["Disease"].value_counts()

    if not disease_counts.empty:

        fig, ax = plt.subplots(figsize=(5,3))

        ax.bar(
            disease_counts.index,
            disease_counts.values,
            width=0.5
        )

        ax.set_xlabel("Disease")
        ax.set_ylabel("Count")

        plt.xticks(rotation=25, fontsize=8)

        st.pyplot(fig)

    else:

        st.info("No prediction history available.")

else:

    st.info("Prediction history file not found.")

st.divider()

# ------------------------------------
# Download Report
# ------------------------------------

csv = summary.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Patient Report",
    data=csv,
    file_name="patient_report.csv",
    mime="text/csv",
    use_container_width=True
)
st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("← Recommendation", use_container_width=True):
        st.switch_page("pages/3_Recommendation.py")

with col2:
    if st.button("Home", use_container_width=True):
        st.switch_page("pages/1Home.py")