"""
Feature building placeholder.

In the internal project, this is where SQL/ETL outputs would be transformed into model-ready tables.
For the public demo we keep it minimal and use synthetic sample CSVs.
"""
from pathlib import Path
import pandas as pd

def load_total(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return df

def load_share(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return df
