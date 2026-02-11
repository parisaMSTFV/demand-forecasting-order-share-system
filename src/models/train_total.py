"""
Train a baseline model for total orders/items (demo).
"""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from src.features.build_features import load_total

def main():
    df = load_total("examples/sample_total.csv").sort_values("date")
    X = df[["campaign_flag","weekday"]]
    y = df["orders_total"]

    tscv = TimeSeriesSplit(n_splits=5)
    maes = []
    for train_idx, test_idx in tscv.split(X):
        model = RandomForestRegressor(n_estimators=300, random_state=42)
        model.fit(X.iloc[train_idx], y.iloc[train_idx])
        pred = model.predict(X.iloc[test_idx])
        maes.append(mean_absolute_error(y.iloc[test_idx], pred))

    print(f"Baseline TimeSeries CV MAE: {sum(maes)/len(maes):.2f}")

if __name__ == "__main__":
    main()
