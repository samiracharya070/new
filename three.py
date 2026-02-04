import streamlit as st
import joblib
import pandas as pd
import random

# Page title
st.title("📰 Nepali News Category Prediction")

# Load trained model
new_model = joblib.load("new_model.joblib")  # your trained model

# Example Nepali news per category
example_news_dict = {
    "अर्थ": [
        "नेपाल सरकारले आगामी आर्थिक वर्षको बजेटमा कृषि र उद्योग क्षेत्रमा लगानी बढाउने घोषणा गरेको छ।",
        "बैंकले नयाँ ऋण योजना सुरु गरेको छ जसले साना व्यवसायलाई सहयोग पुर्याउनेछ।"
    ],
    "राजनीति": [
        "प्रधानमन्त्रीले आज नयाँ नीतिगत कार्यक्रम घोषणा गर्ने भएका छन्।",
        "संसद्मा नयाँ कानून प्रस्ताव पारित भएको छ।"
    ],
    "खेलकुद": [
        "नेपाल क्रिकेट टिमले बंगलादेश विरुद्ध जित हासिल गरेको छ।",
        "फुटबल लिगको उपाधि विजेताले आज प्राप्त गर्नेछ।"
    ],
    "समाज": [
        "काठमाण्डूमा सडक सुरक्षा सम्बन्धी नयाँ अभियान सुरु भएको छ।",
        "सहरी क्षेत्रमा फोहोर व्यवस्थापन सुधार्ने योजना ल्याइएको छ।"
    ]
    # Add more categories and examples if you want
}

# Session state for example text
if "news_text" not in st.session_state:
    st.session_state.news_text = ""

# Example button: pick random category and random news from that category
if st.button("📌 Load Random Example Nepali News"):
    category = random.choice(list(example_news_dict.keys()))
    news_example = random.choice(example_news_dict[category])
    st.session_state.news_text = news_example

# Text input box
news_input = st.text_area(
    "Enter Nepali News Text:",
    value=st.session_state.news_text,
    height=200
)

# Predict button
if st.button("🔍 Predict News Category"):
    if news_input.strip() == "":
        st.warning("Please enter Nepali news text.")
    else:
        prediction = new_model.predict([news_input])
        st.success(f"🧠 Predicted News Category: **{prediction[0]}**")
