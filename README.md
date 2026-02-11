# Demand Forecasting: Total Orders/Items + Province Share

A public, **decision-driven forecasting case study** covering:
- Daily total **orders** and **items** forecasting
- Daily **province-level share** modeling (distribution of orders across provinces)

> Note: Production datasets and internal schemas are intentionally excluded.
> This repository uses **synthetic sample data** to demonstrate methodology and structure.

## What’s inside
- `notebooks/` Clean, runnable notebooks (synthetic data)
- `src/` Minimal Python structure for feature loading, metrics, and training placeholders
- `docs/` Business context, modeling overview, evaluation guidance
- `examples/` Synthetic CSV inputs

## Quickstart
```bash
pip install -r requirements.txt
python src/models/train_total.py
python src/models/train_share.py
```
Open notebooks:
- `notebooks/01_total_orders_forecast.ipynb`
- `notebooks/02_province_share_forecast.ipynb`

## Documentation
- [Business Context](docs/01_business_context.md)
- [Solution Overview](docs/02_solution_overview.md)
- [Modeling Approach](docs/03_modeling_approach.md)
- [Evaluation](docs/04_evaluation.md)

## Contact
LinkedIn: https://www.linkedin.com/in/parisa-mostafavi/  
Email: parisamostafavi23@gmail.com
