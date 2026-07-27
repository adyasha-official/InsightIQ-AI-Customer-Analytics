import sqlite3
import pandas as pd

from src.llm.analyzer import analyze_review


def process_reviews(db_path="data/insightiq.db", limit=100):

    conn = sqlite3.connect(db_path)

    df = pd.read_sql_query(
        f"""
        SELECT
            rowid,
            "Review Text"
        FROM reviews
        LIMIT {limit}
        """,
        conn,
    )

    results = []

    print(f"\nAnalyzing {len(df)} reviews...\n")

    for _, row in df.iterrows():

        try:

            ai = analyze_review(row["Review Text"])

            ai["review_id"] = row["rowid"]

            results.append(ai)

            print(f"✔ Review {row['rowid']}")

        except Exception as e:

            print(f"✘ Review {row['rowid']} : {e}")

    insights = pd.DataFrame(results)
    import json

    if not insights.empty:

      if "themes" in insights.columns:
        insights["themes"] = insights["themes"].apply(
            lambda x: json.dumps(x) if isinstance(x, list) else x
        )

    insights.to_sql(
        "ai_insights",
        conn,
        if_exists="replace",
        index=False,
    )

    conn.close()

    print("\nAI Insights Saved Successfully!")

    return insights