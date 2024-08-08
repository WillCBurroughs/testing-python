import psycopg2

conn = psycopg2.connect(host='localhost', dbname="postgres", user="postgres")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS person(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);
""")

conn.commit()

cur.close()
conn.close()

# Setup database, Add UI 