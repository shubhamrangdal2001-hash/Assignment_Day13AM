"""
Part B: Multi-DataFrame Comparison Report
Creates 3 monthly sales DataFrames, computes summary metrics,
and uses .query(), .nlargest(), .nsmallest() for analysis.
"""

import pandas as pd
import numpy as np

# -----------------------------------------------
# Step 1: Create 3 monthly sales DataFrames
# -----------------------------------------------

january = pd.DataFrame({
    "product": ["Laptop", "Phone", "Headphones", "Tablet", "Smartwatch",
                 "Camera", "Speaker", "Keyboard", "Mouse", "Monitor"],
    "units_sold": [45, 120, 85, 60, 95, 30, 70, 150, 140, 40],
    "unit_price": [55000, 30000, 5000, 25000, 12000, 42000, 4000, 1500, 800, 18000],
    "category": ["Electronics"] * 10
})

february = pd.DataFrame({
    "product": ["Laptop", "Phone", "Headphones", "Tablet", "Smartwatch",
                 "Camera", "Speaker", "Keyboard", "Mouse", "Monitor"],
    "units_sold": [50, 135, 90, 55, 110, 25, 65, 160, 130, 35],
    "unit_price": [55000, 30000, 5000, 25000, 12000, 42000, 4000, 1500, 800, 18000],
    "category": ["Electronics"] * 10
})

march = pd.DataFrame({
    "product": ["Laptop", "Phone", "Headphones", "Tablet", "Smartwatch",
                 "Camera", "Speaker", "Keyboard", "Mouse", "Monitor"],
    "units_sold": [65, 150, 100, 70, 120, 45, 80, 175, 155, 55],
    "unit_price": [55000, 30000, 5000, 25000, 12000, 42000, 4000, 1500, 800, 18000],
    "category": ["Electronics"] * 10
})

# Add revenue column to each month
for month_df in [january, february, march]:
    month_df["revenue"] = month_df["units_sold"] * month_df["unit_price"]

print("=" * 55)
print("     MULTI-MONTH SALES COMPARISON REPORT")
print("=" * 55)

# -----------------------------------------------
# Step 2: Calculate metrics for each month
# -----------------------------------------------
def month_metrics(df, month_name):
    total_revenue = df["revenue"].sum()
    avg_order_value = df["revenue"].mean()
    top_product = df.loc[df["revenue"].idxmax(), "product"]
    return {
        "month": month_name,
        "total_revenue": total_revenue,
        "avg_order_value": round(avg_order_value, 2),
        "top_product": top_product
    }

jan_metrics = month_metrics(january, "January")
feb_metrics = month_metrics(february, "February")
mar_metrics = month_metrics(march, "March")

print("\n--- Monthly Metrics ---")
for m in [jan_metrics, feb_metrics, mar_metrics]:
    print(f"\n{m['month']}:")
    print(f"  Total Revenue:     ₹{m['total_revenue']:,}")
    print(f"  Avg Order Value:   ₹{m['avg_order_value']:,}")
    print(f"  Top Product:       {m['top_product']}")

# -----------------------------------------------
# Step 3: Summary comparison DataFrame
# -----------------------------------------------
summary_df = pd.DataFrame([jan_metrics, feb_metrics, mar_metrics])
summary_df = summary_df.set_index("month")

print("\n--- Summary Comparison DataFrame ---")
print(summary_df)

# -----------------------------------------------
# Step 4: Use .query() for filtering
# -----------------------------------------------
print("\n--- .query() Filtering ---")

# High revenue products in January (revenue > 1,000,000)
jan_high = january.query("revenue > 1_000_000")
print(f"\nJanuary products with revenue > ₹10,00,000:")
print(jan_high[["product", "units_sold", "revenue"]])

# March products with units_sold > 100
mar_popular = march.query("units_sold > 100")
print(f"\nMarch products with units sold > 100:")
print(mar_popular[["product", "units_sold"]])

# -----------------------------------------------
# Step 5: nlargest() and nsmallest() for outliers
# -----------------------------------------------
print("\n--- Outlier Detection ---")

# Combine all 3 months
january["month"] = "January"
february["month"] = "February"
march["month"] = "March"
all_months = pd.concat([january, february, march], ignore_index=True)

print("\nTop 5 highest revenue entries across all months:")
print(all_months.nlargest(5, "revenue")[["month", "product", "units_sold", "revenue"]])

print("\nTop 5 lowest revenue entries across all months:")
print(all_months.nsmallest(5, "revenue")[["month", "product", "units_sold", "revenue"]])

print("\nDone!")
