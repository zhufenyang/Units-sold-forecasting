from lightgbm import LGBMRegressor
from data_preprocessing import load_and_clean_data

def main():
    X, y = load_and_clean_data("retail_store_inventory.csv")

    model = LGBMRegressor(random_state=42)
    model.fit(X, y)

    print("Training finished")

if __name__ == "__main__":
    main()
