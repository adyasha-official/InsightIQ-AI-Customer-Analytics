import sqlite3
import pandas as pd

conn = sqlite3.connect("data/insightiq.db")

df = pd.read_sql_query(
    "SELECT * FROM ai_insights LIMIT 5",
    conn,
)

print(df)

conn.close()