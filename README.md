🌈 MoodMate – Emotion Analyzer

MoodMate is an interactive AI-based emotion recognition system that predicts a user’s mood using a combination of:

Behavioral inputs (emoji-based sliders)

NLP-based text emotion analysis

Optional speech-to-text input

This project integrates Machine Learning, NLP, and a friendly Streamlit UI to help users understand their emotional state more easily.

📌 Features

🔹 Emotion Prediction

Detects emotions such as:

Happy

Sad

Angry

Stressed

Neutral

Excited

🔹 Multiple Input Modes

Answer simple questions using sliders

Type out how you feel

Speak your feelings (optional speech feature)

🔹 Smart ML + NLP Model

TF-IDF based text processing

Logistic Regression / Random Forest classifier

Combined behavioral + text mood scoring

🔹 Interactive User Interface

Emoji sliders

Real-time prediction

Short motivational responses

Simple and clean Streamlit design

🧠 Tech Stack
Component	Technology
Language	Python
UI	Streamlit
ML Model	Random Forest / Logistic Regression
NLP	TF-IDF Vectorizer
Speech Input	SpeechRecognition
Data Processing	Pandas, NumPy
Model Storage	Pickle

📁 Project Structure
MoodMate/
│── app.py               # Main application (Streamlit UI)
│── train_model.py       # Model training script
│── emotion_model.pkl    # Saved ML model
│── emotion_data.csv     # Training dataset
│── requirements.txt     # Required packages
│── README.md            # Documentation

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/AdityaRaj214/MoodMate-Emotion-Analyzer.git

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py

📝 How It Works
1️⃣ User Input

The user interacts with:

4–5 emotional sliders

A text box to describe their mood

Optional speech-to-text input

2️⃣ ML Processing

Text is vectorized using TF-IDF

Model predicts emotion category

Behavioral sliders contribute to a numeric mood score

Both results are combined (hybrid score)

3️⃣ Output

The app displays:

Final emotion prediction

A short personality/mood message

Optional suggestions

📊 Example Output
Predicted Emotion: Happy 😊  
You're having a positive day! Keep the energy flowing ✨

🚀 Future Enhancements

Use Deep Learning models (LSTM, GRU, or BERT)

Weekly mood tracking dashboard

Real-time emotion graph

Mobile app version

More refined emotion categories

Store user history in a secure database

🧑‍💻 Author

Aditya Raj
Computer Science | AI & ML Enthusiast
Open to collaboration and feedback!

🤝 Contributing

Feel free to fork the repository, create issues, or submit pull requests.
