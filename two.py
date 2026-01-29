import streamlit as st
import joblib
import pandas as pd

st.title("Employee Salary Prediction (USD)")

# Load your trained pipeline model
model = joblib.load("salary_model.joblib")  # change filename if needed

# Input fields for the user
experience_level = st.selectbox(
    "Experience Level", 
    ["EN", "MI", "SE", "EX"]  # adjust according to your dataset values
)

employment_type = st.selectbox(
    "Employment Type",
    ["FT", "PT", "CT", "FL"]  # adjust based on your dataset
)

job_title = st.selectbox(
    "Job Title",
    ["Data Scientist", "Data Engineer", "ML Engineer", "Analyst"]  # replace with top job titles from your dataset
)

company_size = st.selectbox(
    "Company Size",
    ["S", "M", "L"]  # small, medium, large
)

# Create a DataFrame for prediction
sample = pd.DataFrame({
    "experience_level": [experience_level],
    "employment_type": [employment_type],
    "job_title": [job_title],
    "company_size": [company_size]
})

# Predict button
if st.button("Predict Salary"):
    prediction = model.predict(sample)
    st.success(f"Predicted Salary (USD): **${prediction[0]:,.2f}**")
