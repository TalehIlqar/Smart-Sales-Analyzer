import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.data_loader import load_sales_data
from app.analyzer import SalesAnalyzer


def print_header(title: str):
    """Print formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def run_analysis(data_path: str = "data/sample_sales.csv"):
    """Run full sales analysis"""
    if not os.path.exists(data_path):
        print(f"Bug@@: Data fayl tapilmadi: {data_path}")
        sys.exit(1)

    dates, products, prices, quantities, regions = load_sales_data(data_path)
    analyzer = SalesAnalyzer(dates, products, prices, quantities, regions)

    print_header("umumi statistika")
    summary = analyzer.get_summary()
    print(f"  Ümumi gəlir:     ${summary['total_revenue']:,.2f}")
    print(f"  Ümumi satış:     {summary['total_quantity']:,} ədəd")
    print(f"  Orta sifariş:    ${summary['avg_order_value']:,.2f}")
    print(f"  Məhsul sayı:     {summary['unique_products']}")
    print(f"  Region sayı:     {summary['unique_regions']}")
    
    for date, revenue, qty in analyzer.analyze_by_day():
        print(f"  {date}:  ${revenue:>12,.2f}  |  {qty:>6} eded")
    
    for month, revenue, qty in analyzer.analyze_by_month():
        print(f"  {month}:  ${revenue:>12,.2f}  |  {qty:>6} eded")
    
    for region, revenue, qty in analyzer.analyze_by_region():
        print(f"  {region:12}:  ${revenue:>12,.2f}  |  {qty:>6} eded")
    
    for i, (product, qty, revenue) in enumerate(analyzer.get_top_products(5), 1):
        print(f"  {i}. {product:20}  {qty:>6} eded  |  ${revenue:>12,.2f}")
    
    weak = analyzer.get_weak_regions(threshold_percent=40)
    if weak:
        for region, revenue, pct in weak:
            print(f"{region:12}:  ${revenue:>12,.2f}  (ortanin {pct})")
    else:
        print("All region sales is normal")


if __name__ == "__main__":
    data_path = os.environ.get("SALES_DATA", "data/sample_sales.csv")
    run_analysis(data_path)
