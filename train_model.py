# app.py
import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("mood_model.pkl")

st.set_page_config(page_title="MoodMate (ML)", page_icon="💭", layout="centered")

st.title("💭 MoodMate (ML Version)")
st.subheader("How are you really feeling today?")

st.markdown("Answer the following questions to find out your current mood 👇")

# Questions
sleep = st.selectbox("🛏️ How did you sleep last night?", ["Great", "Okay", "Poor"])
energy = st.selectbox("⚡ How's your energy level today?", ["High", "Moderate", "Low"])
upset = st.selectbox("😞 Did anything upset you today?", ["No", "A little", "Yes"])
motivation = st.selectbox("🚀 How motivated do you feel today?", ["Very", "Somewhat", "Not at all"])
appetite = st.selectbox("🍽️ How’s your appetite today?", ["Good", "Normal", "Lost"])

# Map inputs to numerical values
map_score = {
    "Great": 2, "Okay": 1, "Poor": 0,
    "High": 2, "Moderate": 1, "Low": 0,
    "No": 2, "A little": 1, "Yes": 0,
    "Very": 2, "Somewhat": 1, "Not at all": 0,
    "Good": 2, "Normal": 1, "Lost": 0
}

features = [
    map_score[sleep],
    map_score[energy],
    map_score[upset],
    map_score[motivation],
    map_score[appetite]
]

# Mood labels
mood_labels = ["😊 Happy", "😐 Neutral", "😞 Sad", "😠 Angry"]

# Submit button
if st.button("🔍 Detect Mood"):
    prediction = model.predict([features])[0]
    st.markdown(f"## Your predicted mood is: **{mood_labels[prediction]}**")
