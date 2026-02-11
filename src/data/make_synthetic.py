"""
Generate synthetic sample data (used for public demo only).
"""
from pathlib import Path
import numpy as np
import pandas as pd

def main(out_dir: str = "examples", n_days: int = 90, seed: int = 42) -> None:
    np.random.seed(seed)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=n_days, freq="D")

    total = pd.DataFrame({
        "date": dates,
        "orders_total": (10000 + np.sin(np.arange(len(dates))/7)*800 + np.random.normal(0, 400, len(dates))).round().astype(int),
        "items_total": (25000 + np.sin(np.arange(len(dates))/7)*1500 + np.random.normal(0, 900, len(dates))).round().astype(int),
        "campaign_flag": np.random.binomial(1, 0.2, len(dates)),
        "weekday": dates.dayofweek,
    })
    total["orders_total"] = total["orders_total"].clip(lower=1000)
    total["items_total"] = total["items_total"].clip(lower=2000)
    total.to_csv(out / "sample_total.csv", index=False)

    provinces = ["Tehran","Isfahan","Fars","Khorasan Razavi","East Azerbaijan","Mazandaran","Khuzestan","Alborz"]
    rows = []
    for d in dates:
        shares = np.random.dirichlet(np.ones(len(provinces))*2)
        for p, s in zip(provinces, shares):
            rows.append({"date": d, "province": p, "share": float(s)})
    pd.DataFrame(rows).to_csv(out / "sample_province_share.csv", index=False)

if __name__ == "__main__":
    main()
