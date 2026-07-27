import sqlite3
import pandas as pd


def run_sql_analysis(db_path="data/insightiq.db"):

    conn = sqlite3.connect(db_path)

    print("\n" + "=" * 60)
    print("SQL ANALYTICS")
    print("=" * 60)

    # Average Rating
    avg_rating = pd.read_sql_query(
        """
        SELECT ROUND(AVG(Rating),2) AS Average_Rating
        FROM reviews;
        """,
        conn,
    )

    print("\nAverage Rating")
    print(avg_rating)

    # Top Departments
    departments = pd.read_sql_query(
        """
        SELECT
            "Department Name",
            COUNT(*) AS Reviews
        FROM reviews
        GROUP BY "Department Name"
        ORDER BY Reviews DESC;
        """,
        conn,
    )

    print("\nReviews by Department")
    print(departments)

    # Rating Distribution
    ratings = pd.read_sql_query(
        """
        SELECT
            Rating,
            COUNT(*) AS Count
        FROM reviews
        GROUP BY Rating
        ORDER BY Rating;
        """,
        conn,
    )

    print("\nRating Distribution")
    print(ratings)

    conn.close()