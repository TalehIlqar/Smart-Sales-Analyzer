import numpy as np


class SalesAnalyzer:
    """NumPy-based sales data analyzer"""
    
    def __init__(self, dates, products, prices, quantities, regions):
        self.dates = dates
        self.products = products
        self.prices = prices
        self.quantities = quantities
        self.regions = regions
        self.revenue = prices * quantities
    
    def analyze_by_day(self) -> dict:
        unique_dates = np.unique(self.dates)
        day_stats = []
        
        for date in unique_dates:
            mask = self.dates == date
            day_revenue = np.sum(self.revenue[mask])
            day_quantity = np.sum(self.quantities[mask])
            day_stats.append((date, day_revenue, day_quantity))
        
        return sorted(day_stats, key=lambda x: x[0])
    
    def analyze_by_month(self) -> dict:
        months = np.array([d[:7] for d in self.dates])
        unique_months = np.unique(months)
        month_stats = []
        
        for month in unique_months:
            mask = months == month
            month_revenue = np.sum(self.revenue[mask])
            month_quantity = np.sum(self.quantities[mask])
            month_stats.append((month, month_revenue, month_quantity))
        
        return sorted(month_stats, key=lambda x: x[0])
    
    def analyze_by_region(self) -> dict:
        unique_regions = np.unique(self.regions)
        region_stats = []
        
        for region in unique_regions:
            mask = self.regions == region
            region_revenue = np.sum(self.revenue[mask])
            region_quantity = np.sum(self.quantities[mask])
            region_stats.append((region, region_revenue, region_quantity))
        
        return region_stats
    
    def get_top_products(self, top_n: int = 5) -> list:
        unique_products = np.unique(self.products)
        product_stats = []
        
        for product in unique_products:
            mask = self.products == product
            total_qty = np.sum(self.quantities[mask])
            total_rev = np.sum(self.revenue[mask])
            product_stats.append((product, total_qty, total_rev))
        
        by_quantity = sorted(product_stats, key=lambda x: x[1], reverse=True)
        return by_quantity[:top_n]
    
    def get_weak_regions(self, threshold_percent: float = 20.0) -> list:
        region_stats = self.analyze_by_region()
        revenues = np.array([r[1] for r in region_stats])
        regions = np.array([r[0] for r in region_stats])
        
        mean_revenue = np.mean(revenues)
        std_revenue = np.std(revenues) if len(revenues) > 1 else 0
        
        weak_mask = revenues < np.percentile(revenues, threshold_percent)
        weak_regions = list(zip(
            regions[weak_mask],
            revenues[weak_mask],
            [f"{(r/mean_revenue*100):.1f}%" for r in revenues[weak_mask]]
        ))
        
        return sorted(weak_regions, key=lambda x: x[1])
    
    def get_summary(self) -> dict:
        return {
            'total_revenue': np.sum(self.revenue),
            'total_quantity': np.sum(self.quantities),
            'avg_order_value': np.mean(self.revenue),
            'unique_products': len(np.unique(self.products)),
            'unique_regions': len(np.unique(self.regions)),
        }
