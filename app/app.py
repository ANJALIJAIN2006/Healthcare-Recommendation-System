import streamlit as st

st.set_page_config(
    page_title="Healthcare Recommendation System",
    page_icon="🏥",
    layout="wide"
)

st.title("Healthcare & Medicine Recommendation System")

st.markdown("---")

st.markdown("""
## Welcome

This application predicts diseases based on patient symptoms and provides personalized healthcare recommendations.

### Features

- Patient Registration
- Disease Prediction
- Medicine Recommendation
- Healthcare Analytics
- BMI Assessment
- Health Risk Analysis

Click any button below to begin.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    if st.button("Patient Registration", use_container_width=True):
        st.switch_page("pages/1Home.py")

    if st.button("Disease Prediction", use_container_width=True):
        st.switch_page("pages/2Prediction.py")

with col2:

    if st.button("Medicine Recommendation", use_container_width=True):
        st.switch_page("pages/3_Recommendation.py")

    if st.button("Analytics Dashboard", use_container_width=True):
        st.switch_page("pages/4_Analytics.py")

st.markdown("---")

st.info("Developed using Python, Streamlit, Machine Learning, Pandas, Scikit-learn, and Matplotlib.")