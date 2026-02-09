import csv
import numpy as np


def load_sales_data(filepath: str) -> tuple:
    """
    Load sales data from CSV file.
    Returns: (dates, products, prices, quantities, regions) as numpy arrays
    """
    dates = []
    products = []
    prices = []
    quantities = []
    regions = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row['date'])
            products.append(row['product'])
            prices.append(float(row['price']))
            quantities.append(int(row['quantity']))
            regions.append(row['region'])
    
    return (
        np.array(dates),
        np.array(products),
        np.array(prices, dtype=np.float64),
        np.array(quantities, dtype=np.int64),
        np.array(regions)
    )
