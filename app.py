import streamlit as st
import pandas as pd
import joblib

# Set the page configuration for the dashboard
st.set_page_config(page_title="Student Score Predictor", page_icon="🎓", layout="wide")

# Load the trained model pipeline
# Use st.cache_resource so it only loads the model once, keeping the app fast
@st.cache_resource
def load_model():
    return joblib.load('student_performance_model.pkl')

model = load_model()

# Build the UI
st.title("🎓 Student Exam Score Predictor")
st.write("This dashboard predicts a student's final exam score based on their study habits, school environment, and lifestyle factors. Adjust the sliders and dropdowns below to see how different variables impact the score!")

st.markdown("---")

# Organize inputs into columns for a better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📚 Study Habits")
    hours_studied = st.slider("Hours Studied per Week", 0, 40, 15)
    attendance = st.slider("Attendance Rate (%)", 0, 100, 85)
    previous_scores = st.slider("Previous Scores (%)", 0, 100, 75)
    tutoring_sessions = st.slider("Tutoring Sessions per Month", 0, 10, 2)
    motivation_level = st.selectbox("Motivation Level", ["Low", "Medium", "High"])

with col2:
    st.subheader("🏫 School & Resources")
    school_type = st.selectbox("School Type", ["Public", "Private"])
    teacher_quality = st.selectbox("Teacher Quality", ["Low", "Medium", "High"])
    access_to_resources = st.selectbox("Access to Resources", ["Low", "Medium", "High"])
    internet_access = st.selectbox("Internet Access", ["Yes", "No"])
    distance_from_home = st.selectbox("Distance from Home", ["Near", "Moderate", "Far"])
    peer_influence = st.selectbox("Peer Influence", ["Positive", "Neutral", "Negative"])

with col3:
    st.subheader("🏠 Lifestyle & Demographics")
    sleep_hours = st.slider("Sleep Hours per Night", 4, 12, 7)
    physical_activity = st.slider("Physical Activity (Hours/Week)", 0, 14, 3)
    extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
    family_income = st.selectbox("Family Income", ["Low", "Medium", "High"])
    parental_involvement = st.selectbox("Parental Involvement", ["Low", "Medium", "High"])
    parental_education = st.selectbox("Parental Education Level", ["High School", "College", "Postgraduate"])
    learning_disabilities = st.selectbox("Learning Disabilities", ["Yes", "No"])
    gender = st.selectbox("Gender", ["Male", "Female"])

st.markdown("---")

# Create a button to trigger the prediction
if st.button("Predict Exam Score 🚀", type="primary"):
    
    # Map the user inputs to a dictionary matching our training data columns
    input_data = {
        'Hours_Studied': hours_studied,
        'Attendance': attendance,
        'Parental_Involvement': parental_involvement,
        'Access_to_Resources': access_to_resources,
        'Extracurricular_Activities': extracurricular,
        'Sleep_Hours': sleep_hours,
        'Previous_Scores': previous_scores,
        'Motivation_Level': motivation_level,
        'Internet_Access': internet_access,
        'Tutoring_Sessions': tutoring_sessions,
        'Family_Income': family_income,
        'Teacher_Quality': teacher_quality,
        'School_Type': school_type,
        'Peer_Influence': peer_influence,
        'Physical_Activity': physical_activity,
        'Learning_Disabilities': learning_disabilities,
        'Parental_Education_Level': parental_education,
        'Distance_from_Home': distance_from_home,
        'Gender': gender
    }
    
    # Convert the dictionary into a Pandas DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Predict the score using the loaded model pipeline
    predicted_score = model.predict(input_df)[0]
    
    # Display the result
    st.success("Prediction Complete!")
    st.metric(label="Predicted Exam Score", value=f"{predicted_score:.1f}%")
