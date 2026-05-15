from sqlalchemy import text
from database import engine

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);
"""

create_tests_table = """
CREATE TABLE IF NOT EXISTS tests (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
"""

create_sessions_table = """
CREATE TABLE IF NOT EXISTS test_sessions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    test_id INT REFERENCES tests(id),
    start_time TIMESTAMP,
    end_time TIMESTAMP
);
"""

create_responses_table = """
CREATE TABLE IF NOT EXISTS test_responses (
    id SERIAL PRIMARY KEY,
    session_id INT REFERENCES test_sessions(id),
    question_id INT,
    topic TEXT,
    is_correct BOOLEAN,
    time_spent FLOAT
);
"""

with engine.connect() as conn:
    conn.execute(text(create_users_table))
    conn.execute(text(create_tests_table))
    conn.execute(text(create_sessions_table))
    conn.execute(text(create_responses_table))
    conn.commit()

print("Tables created successfully!")
