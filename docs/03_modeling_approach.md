# Modeling Approach (High-Level)

## Total Orders/Items
- Baselines: moving average / weekday seasonality
- ML models (demo): tree-based regression using time-aware splits
- Future extension: adding lag features, holidays, price/fx signals, campaign signals

## Province Share
- Goal: estimate daily shares by province (must sum to 1)
- Demo workflow: feature preparation + share table creation
- Future extension: constrained models (e.g., softmax regression), hierarchical time series, reconciliation
