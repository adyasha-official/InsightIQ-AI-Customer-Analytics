from src.utils.load_data import load_dataset


def main():

    df = load_dataset("data/Womens Clothing E-Commerce Reviews.csv")

    print("\nFirst Five Rows:\n")
    print(df.head())

    print("\nDataset Information:\n")
    print(df.info())


if __name__ == "__main__":
    main()