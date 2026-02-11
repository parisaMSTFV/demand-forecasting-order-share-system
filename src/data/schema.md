# Sample Data Schema

This repository uses **synthetic sample data** for demonstration.

## sample_total.csv
- `date` (YYYY-MM-DD): day
- `orders_total` (int): total daily orders
- `items_total` (int): total daily items
- `campaign_flag` (0/1): whether a major campaign was active
- `weekday` (0-6): Monday=0 ... Sunday=6

## sample_province_share.csv
- `date` (YYYY-MM-DD): day
- `province` (string): province name
- `share` (float): share of daily orders (sums to 1 per day in synthetic data)
