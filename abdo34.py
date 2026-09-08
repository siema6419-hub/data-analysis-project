import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    name TEXT,
    score INTEGER
)
""")

cursor.execute("""
INSERT INTO students VALUES
('Ali',85)
""")

conn.commit()

result = cursor.execute(
    "SELECT * FROM students"
)

print(result.fetchall())

conn.close()
