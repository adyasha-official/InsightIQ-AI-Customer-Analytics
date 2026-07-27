from src.utils.load_data import load_dataset
from src.utils.clean_data import clean_dataset


def main():

    df = load_dataset(
        "data/Womens Clothing E-Commerce Reviews.csv"
    )

    df = clean_dataset(df)

    print("\nClean Dataset Preview\n")
    print(df.head())

    print("\nDataset Shape")
    print(df.shape)


if __name__ == "__main__":
    main()