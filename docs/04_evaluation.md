# Evaluation

Evaluation should be time-aware (backtesting), not random split.

Recommended metrics:
- MAE / RMSE for totals
- MAPE for interpretability (with care for low-volume days)
- For shares: MAE by province + stability of sum-to-1 constraint (in production)
