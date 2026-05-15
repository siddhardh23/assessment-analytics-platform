from fastapi import FastAPI
from sqlalchemy import text
from database import engine

app = FastAPI()


@app.get("/")
def home():
    return {"message": "EduTest Analytics API Running"}


@app.get("/kpi/overall")
def overall_accuracy():

    query = text("""
        SELECT ROUND(AVG(is_correct::int) * 100, 2)
        AS overall_accuracy
        FROM test_responses
    """)

    with engine.connect() as conn:
        result = conn.execute(query).scalar()

    return {"overall_accuracy": result}


@app.get("/kpi/topics")
def topic_accuracy():

    query = text("""
        SELECT
            topic,
            ROUND(AVG(is_correct::int) * 100, 2)
            AS accuracy
        FROM test_responses
        GROUP BY topic
        ORDER BY accuracy DESC
    """)

    with engine.connect() as conn:

        result = conn.execute(query)

        data = []

        for row in result:
            data.append({
                "topic": row.topic,
                "accuracy": row.accuracy
            })

    return data
@app.get("/user/{user_id}/performance")
def user_performance(user_id: int):

    query = text("""
        SELECT
            ts.user_id,

            ROUND(AVG(tr.is_correct::int) * 100::numeric, 2) AS accuracy,

            ROUND(AVG(tr.time_spent)::numeric, 2) AS avg_time_spent

        FROM test_sessions ts

        JOIN test_responses tr
            ON ts.id = tr.session_id

        WHERE ts.user_id = :user_id

        GROUP BY ts.user_id
    """)

    with engine.connect() as conn:

        result = conn.execute(
            query,
            {"user_id": user_id}
        ).mappings().first()

    if result is None:
        return {"error": "User not found"}

    return dict(result)

@app.get("/user/{user_id}/feedback")
def user_feedback(user_id: int):

    query = text("""
        SELECT
            topic,
            ROUND(
                AVG(is_correct::int) * 100,
                2
            ) AS accuracy

        FROM test_sessions ts

        JOIN test_responses tr
            ON ts.id = tr.session_id

        WHERE ts.user_id = :user_id

        GROUP BY topic
    """)

    with engine.connect() as conn:

        results = conn.execute(
            query,
            {"user_id": user_id}
        ).mappings().all()

    if not results:
        return {"error": "User not found"}

    weak_topics = []
    strong_topics = []

    for row in results:

        if row["accuracy"] < 60:
            weak_topics.append(row["topic"])

        else:
            strong_topics.append(row["topic"])

    feedback = ""

    if strong_topics:
        feedback += (
            f"Strong performance in "
            f"{', '.join(strong_topics)}. "
        )

    if weak_topics:
        feedback += (
            f"Needs improvement in "
            f"{', '.join(weak_topics)}."
        )

    return {
        "user_id": user_id,
        "feedback": feedback
    }