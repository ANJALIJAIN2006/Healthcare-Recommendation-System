import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
disease_df = pd.read_csv("data/raw/disease.csv")
medicine_df = pd.read_csv("data/raw/medicine.csv")
lifestyle_df = pd.read_csv("data/raw/lifestyle.csv")

print("="*60)
print("DISEASE DATASET")
print("="*60)

# First 5 rows
print("\nFirst 5 Rows:")
print(disease_df.head())

# Shape
print("\nDataset Shape:")
print(disease_df.shape)

# Columns
print("\nColumns:")
print(disease_df.columns)

# Data types
print("\nData Types:")
print(disease_df.dtypes)

# Missing values
print("\nMissing Values:")
print(disease_df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(disease_df.duplicated().sum())

# Statistics
print("\nStatistics:")
print(disease_df.describe())

# Disease frequency
print("\nDisease Frequency:")
print(disease_df["disease"].value_counts())
# Disease Frequency Bar Chart

disease_df["disease"].value_counts().plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Disease Frequency")
plt.xlabel("Disease")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Disease Distribution Pie Chart

disease_df["disease"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7,7)
)

plt.title("Disease Distribution")
plt.ylabel("")
plt.show()
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

symptom_count = disease_df[symptoms].sum()

print("\nSymptom Frequency")
print(symptom_count)
most_common = disease_df["disease"].mode()[0]

print("\nMost Common Disease:", most_common)