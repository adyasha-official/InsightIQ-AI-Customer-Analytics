import pandas as pd


def load_dataset(path):
    """
    Load the review dataset from CSV.
    """

    df = pd.read_csv(path)

    print("=" * 60)
    print("DATASET LOADED SUCCESSFULLY")
    print("=" * 60)
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")
    print()

    return df