import pandas as pd
from os import path
from validation import AustralianState


def _read_electricity_prices() -> pd.DataFrame:
    """Read the electricity prices CSV file and return a pandas DataFrame."""
    csv_path = "data/coding_challenge_prices.csv"

    if not path.exists(csv_path):
        raise FileNotFoundError(f"File {csv_path} not found!")

    # Read the CSV file
    df = pd.read_csv(csv_path)
    # Normalise the state column to uppercase:
    df["state"] = df["state"].str.upper()
    return df


def mean_price_by_state(state: AustralianState) -> float:
    df = _read_electricity_prices()
    return float(df[df["state"] == state]["price"].mean())
