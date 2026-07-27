import pandas as pd


def clean_dataset(df):
    """
    Clean the raw review dataset.
    """

    print("\nCleaning Dataset...")

    # Remove unwanted index column
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Remove duplicates
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    # Remove rows without review text
    missing_reviews = df["Review Text"].isna().sum()
    df = df.dropna(subset=["Review Text"])

    # Fill missing titles
    df["Title"] = df["Title"].fillna("No Title")

    # Fill missing categories
    for col in [
        "Division Name",
        "Department Name",
        "Class Name"
    ]:
        df[col] = df[col].fillna("Unknown")

    # Strip whitespace
    object_cols = df.select_dtypes(include="object").columns

    for col in object_cols:
        df[col] = df[col].str.strip()

    print(f"Duplicates Removed      : {duplicates}")
    print(f"Missing Reviews Removed : {missing_reviews}")
    print(f"Final Rows              : {len(df)}")

    return df