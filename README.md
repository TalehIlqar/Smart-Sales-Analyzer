# Smart Sales Analyzer 📊

Sales analysis tool built with NumPy. Analyzes sales data by day/month/region, top-selling products, and underperforming regions.

## Usage

### With Docker (recommended)

```bash
./start
```

This command builds the Docker image and runs the analysis.

### Run locally

```bash
pip install -r requirements.txt
python main.py
```

## Data format

`data/sample_sales.csv` – CSV format with columns:
- `date` – date (YYYY-MM-DD)
- `product` – product name
- `price` – price
- `quantity` – quantity
- `region` – region

You can add your own data to the `data/` folder and point to it using the `SALES_DATA` environment variable.
