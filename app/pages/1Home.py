import streamlit as st

st.set_page_config(
    page_title="Patient Registration",
    layout="wide"
)

st.title("Patient Registration")
st.write("Enter patient details to begin disease prediction.")

# ------------------------------------
# Patient Information
# ------------------------------------

with st.container(border=True):

    st.subheader("Patient Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Patient Name")
        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=25
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

    with col2:

        height = st.number_input(
            "Height (cm)",
            min_value=100,
            max_value=220,
            value=170
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=20,
            max_value=200,
            value=65
        )

        blood = st.selectbox(
            "Blood Group",
            [
                "A+","A-",
                "B+","B-",
                "AB+","AB-",
                "O+","O-"
            ]
        )

# ------------------------------------
# Symptoms
# ------------------------------------

st.write("")

with st.container(border=True):

    st.subheader("Symptoms")

    c1, c2, c3 = st.columns(3)

    with c1:
        fever = st.checkbox("Fever")
        cough = st.checkbox("Cough")
        headache = st.checkbox("Headache")

    with c2:
        fatigue = st.checkbox("Fatigue")
        body_pain = st.checkbox("Body Pain")
        sore_throat = st.checkbox("Sore Throat")

    with c3:
        nausea = st.checkbox("Nausea")
        vomiting = st.checkbox("Vomiting")
        diarrhea = st.checkbox("Diarrhea")

# ------------------------------------
# Save
# ------------------------------------

st.write("")

if st.button(
    "Save Patient Details",
    use_container_width=True
):
    st.session_state["patient"] = {
        "name": name,
        "age": age,
        "gender": gender,
        "blood": blood,
        "height": height,
        "weight": weight,
        "fever": fever,
        "cough": cough,
        "headache": headache,
        "fatigue": fatigue,
        "body_pain": body_pain,
        "sore_throat": sore_throat,
        "nausea": nausea,
        "vomiting": vomiting,
        "diarrhea": diarrhea
    }

    st.success("Patient details saved successfully!")

st.write("")

if st.button(
    "Next → Prediction",
    use_container_width=True
):
    st.switch_page("pages/2Prediction.py")  # Use your actual filename