# 📊 Assessment Analytics Platform

An end-to-end **data analytics + backend + dashboard system** that simulates a real-world SaaS assessment platform where users take tests, and their performance is analyzed using SQL-based analytics and rule-based recommendation logic.

This project demonstrates **data engineering, backend API design, analytics engineering, and dashboard development**.

---

# 🧠 System Overview

The platform simulates an online assessment system where:

1. Users take tests
2. Responses are stored in PostgreSQL
3. SQL queries analyze performance
4. FastAPI exposes analytics endpoints
5. Streamlit visualizes insights
6. Rule-based logic generates personalized feedback

---

# 🔄 Architecture / Workflow

---

# 📌 Data Flow Explanation

### 1. User Interaction
- Users take assessments
- Each answer is stored as a response

### 2. Data Storage
- PostgreSQL stores:
  - users
  - tests
  - test_sessions
  - test_responses

### 3. Analytics Layer
SQL queries compute:
- accuracy per topic
- overall performance
- time spent per question
- weak & strong areas

### 4. API Layer (FastAPI)
- Exposes analytics as JSON endpoints
- Used by frontend/dashboard

### 5. Visualization Layer (Streamlit)
- Displays:
  - KPIs
  - charts
  - user performance
  - insights

### 6. Recommendation Engine
- Rule-based logic generates feedback:
  - weak topics
  - strong topics
  - improvement suggestions

---

# ⚙️ Tech Stack

- 🐍 Python
- ⚡ FastAPI
- 🗄️ PostgreSQL
- 🔗 SQLAlchemy
- 📊 Streamlit
- 📦 Uvicorn
- 🧪 Faker (for synthetic data generation)

---

# 📊 Key Features

## 📌 Analytics Engine
- Topic-wise performance tracking
- Overall accuracy calculation
- Time spent analysis
- User-level KPIs

## 📌 REST APIs
- `/kpi/overall`
- `/kpi/topics`
- `/user/{id}/performance`
- `/user/{id}/feedback`

## 📌 Dashboard
- Interactive Streamlit dashboard
- Real-time KPI visualization
- User performance breakdown

## 📌 Recommendation System
- Rule-based feedback engine
- Weak topic detection (<60% accuracy)
- Strong topic identification
- Personalized improvement suggestions

---

# 🧠 AI / Recommendation Logic

This project uses a **rule-based intelligent system**:

- If accuracy < 60% → weak area
- If accuracy ≥ 60% → strong area

This simulates early-stage AI systems used in startups before integrating LLMs.

---

# 🗃️ Database Schema

### users
- id
- name
- email

### tests
- id
- name

### test_sessions
- id
- user_id
- test_id

### test_responses
- id
- session_id
- question_id
- topic
- is_correct
- time_spent

---

# 🚀 API Endpoints

## 📍 Overall Accuracy

Returns overall performance across all users.

---

## 📍 Topic Accuracy

Returns accuracy grouped by topic.

---

## 📍 User Performance

Returns:
- accuracy
- average time spent

---

## 📍 AI Feedback

Returns personalized recommendations.

---

# 📈 Example Output

```json
{
"user_id": 1,
"feedback": "Strong performance in Python, ML. Needs improvement in SQL."
}
📈 Future Improvements
LLM-based AI feedback system
Real-time dashboards
Authentication system
Advanced ML-based analytics