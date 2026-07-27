from src.utils.load_data import load_dataset
from src.utils.clean_data import clean_dataset
from src.database.db import save_to_database
from src.analysis.sql_analysis import run_sql_analysis


def main():

    df = load_dataset(
        "data/Womens Clothing E-Commerce Reviews.csv"
    )

    df = clean_dataset(df)

    save_to_database(df)

    run_sql_analysis()

    print("\nPipeline Completed Successfully!")


if __name__ == "__main__":
    main()