import streamlit as st

st.set_page_config(page_title="MoodMate", page_icon="💭", layout="centered")

st.title("💭 MoodMate")
st.subheader("How are you really feeling today?")

st.markdown("Answer the following questions to find out your current mood 👇")

# Questions with dropdown options
sleep = st.selectbox("🛏️ How did you sleep last night?", ["Great", "Okay", "Poor"])
energy = st.selectbox("⚡ How's your energy level today?", ["High", "Moderate", "Low"])
upset = st.selectbox("😞 Did anything upset you today?", ["No", "A little", "Yes"])
motivation = st.selectbox("🚀 How motivated do you feel today?", ["Very", "Somewhat", "Not at all"])
appetite = st.selectbox("🍽️ How's your appetite today?", ["Good", "Normal", "Lost"])

# Mood mapping function
def detect_mood(sleep, energy, upset, motivation, appetite):
    score = 0

    if sleep == "Great": score += 2
    elif sleep == "Okay": score += 1

    if energy == "High": score += 2
    elif energy == "Moderate": score += 1

    if upset == "No": score += 2
    elif upset == "A little": score += 1

    if motivation == "Very": score += 2
    elif motivation == "Somewhat": score += 1

    if appetite == "Good": score += 2
    elif appetite == "Normal": score += 1

    # Determine mood from score
    if score >= 9:
        return "😊 Happy"
    elif 6 <= score < 9:
        return "😐 Neutral"
    elif 3 <= score < 6:
        return "😞 Sad"
    else:
        return "😠 Angry"

# Submit button
if st.button("🔍 Detect Mood"):
    mood = detect_mood(sleep, energy, upset, motivation, appetite)
    st.markdown(f"## Your current mood is: **{mood}**")
