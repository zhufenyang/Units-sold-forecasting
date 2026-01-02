import pandas as pd

def load_and_clean_data(path):
    """
    Load raw data and apply preprocessing.
    """
    df = pd.read_csv(path)

    # TODO: copy preprocessing logic from notebook
    y = df["units_sold"]
    X = df.drop(columns=["units_sold"])

    return X, y
