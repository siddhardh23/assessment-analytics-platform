from faker import Faker
from random import randint, choice, uniform
from datetime import datetime, timedelta
from sqlalchemy import text
from database import engine

fake = Faker()

topics = ["Python", "SQL", "Math", "Statistics", "ML"]

with engine.connect() as conn:

    # USERS
    for _ in range(50):
        conn.execute(
            text("""
                INSERT INTO users (name, email)
                VALUES (:name, :email)
            """),
            {
                "name": fake.name(),
                "email": fake.unique.email()
            }
        )

    # TESTS
    test_names = [
        "Python Assessment",
        "SQL Assessment",
        "ML Assessment",
        "Statistics Test",
        "Data Science Test"
    ]

    for name in test_names:
        conn.execute(
            text("""
                INSERT INTO tests (name)
                VALUES (:name)
            """),
            {"name": name}
        )

    conn.commit()

    # SESSIONS + RESPONSES
    for _ in range(200):

        user_id = randint(1, 50)
        test_id = randint(1, 5)

        start_time = fake.date_time_this_year()
        end_time = start_time + timedelta(minutes=randint(10, 60))

        result = conn.execute(
            text("""
                INSERT INTO test_sessions
                (user_id, test_id, start_time, end_time)
                VALUES (:user_id, :test_id, :start_time, :end_time)
                RETURNING id
            """),
            {
                "user_id": user_id,
                "test_id": test_id,
                "start_time": start_time,
                "end_time": end_time
            }
        )

        session_id = result.scalar()

        # responses
        for q in range(20):

            conn.execute(
                text("""
                    INSERT INTO test_responses
                    (session_id, question_id, topic, is_correct, time_spent)
                    VALUES
                    (:session_id, :question_id, :topic,
                     :is_correct, :time_spent)
                """),
                {
                    "session_id": session_id,
                    "question_id": q + 1,
                    "topic": choice(topics),
                    "is_correct": choice([True, False]),
                    "time_spent": round(uniform(10, 90), 2)
                }
            )

    conn.commit()

print("Sample data inserted successfully!")