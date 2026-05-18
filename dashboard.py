import requests
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="EduTest Analytics",
    layout="wide"
)

st.title("📊 EduTest Analytics Dashboard")

# -----------------------------------
# API BASE URL
# -----------------------------------

API_URL = "https://assessment-analytics-platform.onrender.com"

# -----------------------------------
# OVERALL KPI
# -----------------------------------

overall = requests.get(
    f"{API_URL}/kpi/overall"
).json()

st.metric(
    label="Overall Accuracy",
    value=f"{overall['overall_accuracy']} %"
)

# -----------------------------------
# TOPIC PERFORMANCE
# -----------------------------------

st.subheader("Topic-wise Accuracy")

topics = requests.get(
    f"{API_URL}/kpi/topics"
).json()

df_topics = pd.DataFrame(topics)

st.bar_chart(
    df_topics.set_index("topic")
)

# -----------------------------------
# USER ANALYTICS
# -----------------------------------

st.subheader("User Performance")

user_id = st.number_input(
    "Enter User ID",
    min_value=1,
    max_value=50,
    value=1
)

user_perf = requests.get(
    f"{API_URL}/user/{user_id}/performance"
).json()

col1, col2 = st.columns(2)

col1.metric(
    "Accuracy",
    f"{user_perf['accuracy']} %"
)

col2.metric(
    "Average Time",
    f"{user_perf['avg_time_spent']} sec"
)

# -----------------------------------
# AI FEEDBACK
# -----------------------------------

st.subheader("AI Feedback")

feedback = requests.get(
    f"{API_URL}/user/{user_id}/feedback"
).json()

st.success(
    feedback["feedback"]
)