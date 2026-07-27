import sqlite3
import pandas as pd


def save_to_database(df, db_path="data/insightiq.db"):
    """
    Save cleaned dataframe into SQLite database.
    """

    conn = sqlite3.connect(db_path)

    df.to_sql(
        "reviews",
        conn,
        if_exists="replace",
        index=False
    )

    conn.commit()
    conn.close()

    print("\nSQLite Database Created Successfully!")
    print(f"Database : {db_path}")
    print(f"Table     : reviews")