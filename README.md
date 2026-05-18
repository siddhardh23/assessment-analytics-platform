# 📊 Assessment Analytics Platform

A cloud-deployed analytics platform that simulates a real-world assessment system where user test performance is processed, analyzed, and exposed through REST APIs and interactive dashboards.

The project demonstrates backend analytics workflows, SQL-based KPI generation, API development, dashboard visualization, and rule-based recommendation logic.

---

# 🚀 Live API

🔗 https://assessment-analytics-platform.onrender.com

API Documentation:

🔗 https://assessment-analytics-platform.onrender.com/docs

---

# 📸 Screenshots

## Dashboard

![Dashboard](screenshots/dashboard.png)

## API Documentation

![API Docs](screenshots/api-docs.png)

## Example API Response

![API Response](screenshots/api-response.png)

---

# 🧠 System Workflow

```text
Users/Test Responses
        ↓
PostgreSQL Database (Neon)
        ↓
SQL Analytics Processing
        ↓
FastAPI Backend APIs
        ↓
Streamlit Dashboard
        ↓
Rule-Based Feedback Engine
```

---

# ⚙️ Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Streamlit
- Uvicorn
- Faker
- Render
- Neon PostgreSQL

---

# 📊 Core Features

## Analytics Engine
- Topic-wise performance analysis
- Overall accuracy calculation
- User-level KPI tracking
- Average time spent analysis

## REST APIs
- `/kpi/overall`
- `/kpi/topics`
- `/user/{id}/performance`
- `/user/{id}/feedback`

## Dashboard & Visualization
- Interactive KPI dashboard
- Performance charts
- User analytics visualization
- Personalized insights

## Recommendation Engine
- Rule-based feedback generation
- Weak topic detection
- Personalized improvement suggestions

---

# 🗃️ Database Schema

## users
Stores user information.

## tests
Stores assessment details.

## test_sessions
Tracks user test attempts.

## test_responses
Stores question-level responses, accuracy, and time spent.

---

# 🔍 Key Concepts Implemented

- Relational database design
- SQL aggregations and joins
- KPI analytics
- REST API development
- Backend-to-dashboard integration
- Cloud deployment workflows
- Rule-based recommendation systems

---

# 📈 Example API Response

```json
{
  "user_id": 1,
  "feedback": "Strong performance in Python, ML. Needs improvement in SQL."
}
```

---

# ☁️ Deployment

## Backend
Deployed using Render.

## Database
Hosted using Neon PostgreSQL.

---

# 🚀 Future Improvements

- LLM-based AI feedback generation
- Authentication & user management
- Advanced ML-based recommendations
- Real-time analytics pipelines
- Docker containerization