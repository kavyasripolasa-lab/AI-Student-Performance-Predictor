import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------- DYNAMIC BACKGROUND ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #e3f2fd, #f3e5f5, #e8f5e9, #fff3e0);
    background-size: 400% 400%;
    animation: gradient 12s ease infinite;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.75);
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
data = pd.read_csv("student_data.csv")
model = joblib.load("student_performance_model.pkl")

# ---------------- TITLE ----------------
st.markdown(
    '<div class="main-title">🎓 AI Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered student performance analysis and prediction</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- STUDENT SEARCH ----------------
st.subheader("👨‍🎓 Select Student")

col1, col2 = st.columns(2)

with col1:
    student_name = st.selectbox(
        "Student Name",
        sorted(data["Student_Name"].unique())
    )

with col2:
    student_rows = data[data["Student_Name"] == student_name]

    roll_number = st.selectbox(
        "Roll Number",
        student_rows["Roll_Number"].tolist()
    )

# Find selected student
student = data[
    (data["Student_Name"] == student_name) &
    (data["Roll_Number"] == roll_number)
]

if not student.empty:

    student = student.iloc[0]

    st.divider()

    # ---------------- STUDENT DETAILS ----------------
    st.subheader("📋 Student Performance Details")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📅 Attendance", f"{student['Attendance']}%")
    col2.metric("📝 Assignment", f"{student['Assignment_Score']}")
    col3.metric("📚 Mid Marks", f"{student['Mid_Marks']}")
    col4.metric("🎓 Previous GPA", f"{student['Previous_GPA']}")

    st.divider()

    # ---------------- AI PREDICTION ----------------
    if st.button("🔮 Predict Student Performance", use_container_width=True):

        features = [[
            student["Attendance"],
            student["Study_Hours"],
            student["Assignment_Score"],
            student["Mid_Marks"],
            student["Previous_GPA"]
        ]]

        prediction = model.predict(features)[0]
        prediction = max(0, min(100, prediction))

        # Performance category
        if prediction >= 85:
            performance = "Excellent 🌟"
            risk = "Low 🟢"
        elif prediction >= 70:
            performance = "Good 👍"
            risk = "Low 🟢"
        elif prediction >= 50:
            performance = "Needs Improvement ⚠️"
            risk = "Medium 🟡"
        else:
            performance = "At Risk 🔴"
            risk = "High 🔴"

        # ---------------- RESULT ----------------
        st.subheader("🤖 AI Prediction")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Predicted Final Score",
            f"{prediction:.1f}%"
        )

        c2.metric(
            "Performance",
            performance
        )

        c3.metric(
            "Risk Level",
            risk
        )

        # ---------------- CHART ----------------
        st.subheader("📊 Performance Overview")

        chart_data = pd.DataFrame({
            "Category": [
                "Attendance",
                "Assignment",
                "Mid Marks",
                "Previous GPA"
            ],
            "Score": [
                student["Attendance"],
                student["Assignment_Score"],
                student["Mid_Marks"],
                student["Previous_GPA"] * 10
            ]
        })

        st.bar_chart(
            chart_data.set_index("Category")
        )

        # ---------------- SUGGESTIONS ----------------
        st.subheader("💡 Personalized Suggestions")

        suggestions = []

        if student["Attendance"] < 75:
            suggestions.append(
                "📅 Improve attendance to maintain consistent learning."
            )

        if student["Study_Hours"] < 2:
            suggestions.append(
                "📚 Increase daily study time gradually."
            )

        if student["Assignment_Score"] < 60:
            suggestions.append(
                "📝 Focus more on completing and improving assignments."
            )

        if student["Mid_Marks"] < 60:
            suggestions.append(
                "📖 Spend more time preparing for examinations."
            )

        if student["Previous_GPA"] < 7:
            suggestions.append(
                "🎯 Set small weekly academic goals to improve GPA."
            )

        if not suggestions:
            suggestions.append(
                "🌟 Excellent work! Maintain your current study habits."
            )

        for suggestion in suggestions:
            st.info(suggestion)

        # ---------------- STUDENT PROFILE ----------------
        st.subheader("👤 Student Profile")

        profile = {
    "Student Name": student["Student_Name"],
    "Roll Number": student["Roll_Number"],
    "Attendance": f'{student["Attendance"]}%',
    "Study Hours": f'{student["Study_Hours"]} hours/day',
    "Assignment Score": student["Assignment_Score"],
    "Mid Marks": student["Mid_Marks"],
    "Previous GPA": student["Previous_GPA"],
    "Final Score": student["Final_Score"]
}