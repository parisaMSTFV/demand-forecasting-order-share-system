"""
Province share modeling placeholder (demo).

For real production, this could be a hierarchical model or constrained regression ensuring shares sum to 1.
In the public demo we focus on workflow rather than production constraints.
"""
import pandas as pd
from src.features.build_features import load_share

def main():
    df = load_share("examples/sample_province_share.csv").sort_values(["date","province"])
    # Placeholder: show daily shares by province
    pivot = df.pivot_table(index="date", columns="province", values="share")
    print(pivot.tail())

if __name__ == "__main__":
    main()
