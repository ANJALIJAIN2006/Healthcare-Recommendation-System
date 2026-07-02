# Personalized Healthcare & Medicine Recommendation System

A Machine Learning-based web application that predicts diseases based on patient symptoms and provides personalized healthcare recommendations, BMI analysis, health risk assessment, and analytics using Streamlit.

---

## Project Overview

This project is designed to assist users in identifying possible diseases based on selected symptoms. It also calculates the patient's Body Mass Index (BMI), estimates health risk, recommends medicines and lifestyle suggestions, and provides an analytics dashboard.

---

## Features

- Patient Registration
- Disease Prediction using Machine Learning
- Prediction Confidence Score
- BMI Calculation
- Health Risk Assessment
- Medicine Recommendation
- Lifestyle Recommendation
- Patient Summary
- Healthcare Analytics Dashboard
- Prediction History
- Disease Distribution Chart
- Download Patient Report (CSV)

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

## Project Structure

```
Healthcare-Recommendation-System/
│
├── app/
│   ├── app.py
│   └── pages/
│       ├── 1_Home.py
│       ├── 2_Prediction.py
│       ├── 3_Recommendation.py
│       └── 4_Analytics.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── history/
│   └── history.csv
│
├── models/
│   ├── disease_model.pkl
│   └── label_encoder.pkl
│
├── notebooks/
│
├── reports/
│
├── src/
│   ├── bmi.py
│   ├── eda.py
│   ├── predict.py
│   └── risk.py
│
├── requirements.txt
└── README.md
```

---

## Dataset

The machine learning model is trained using a symptom-based dataset containing patient symptoms and disease labels.

Example Symptoms:

- Fever
- Cough
- Headache
- Fatigue
- Body Pain
- Sore Throat
- Nausea
- Vomiting
- Diarrhea

---

## Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Model Workflow:

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Disease Prediction

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Healthcare-Recommendation-System.git
```

Move into the project directory:

```bash
cd Healthcare-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/app.py
```

---

## Application Workflow

1. Register Patient
2. Enter Symptoms
3. Predict Disease
4. View BMI & Health Risk
5. Get Medicine Recommendation
6. View Analytics Dashboard
7. Download Patient Report

---

## Screens

- Home Page
- Patient Registration
- Disease Prediction
- Medicine Recommendation
- Analytics Dashboard

---

## Future Improvements

- Login Authentication
- Database Integration (SQLite/MySQL)
- PDF Report Generation
- Email Notifications
- Appointment Booking
- AI Chatbot Integration
- Real-Time Disease Dataset
- Interactive Plotly Dashboards

---

## Learning Outcomes

This project demonstrates:

- Machine Learning
- Data Preprocessing
- Model Serialization using Joblib
- Streamlit Web Application Development
- Data Visualization
- Python Programming
- Healthcare Data Analysis

---

## Author

**Anjali Jain**

Cybersecurity & AI Enthusiast

---

## License

This project is developed for educational and academic purposes.
=======
# Healthcare-Recommendation-System
A Machine Learning-based web application that predicts diseases based on patient symptoms and provides personalized healthcare recommendations, BMI analysis, health risk assessment, and analytics using Streamlit.

