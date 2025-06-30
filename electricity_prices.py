import pandas as pd
from os import path
from validation import AustralianState

CSV_PATH = "data/coding_challenge_prices.csv"


def _read_electricity_prices() -> pd.DataFrame:
    """Read the electricity prices CSV file and return a pandas DataFrame."""

    if not path.exists(CSV_PATH):
        raise FileNotFoundError(f"File {CSV_PATH} not found!")

    df = pd.read_csv(CSV_PATH)
    # Normalise the state column to uppercase:
    df["state"] = df["state"].str.upper()

    return df


def mean_price_by_state(state: AustralianState) -> float:
    df = _read_electricity_prices()
    result = df[df["state"] == state]["price"].mean()
    if pd.isna(result):
        raise ValueError(f"State {state} not found in data")
    return float(result)
