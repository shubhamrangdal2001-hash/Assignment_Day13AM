"""
Part A: E-Commerce Product Analyzer
Creates a product DataFrame, performs loc/iloc operations,
filters into sub-DataFrames, and exports to CSV files.
"""

import pandas as pd
import numpy as np

# -----------------------------------------------
# Step 1: Create the DataFrame with 20+ products
# -----------------------------------------------
data = {
    "name": [
        "Samsung Galaxy S23", "Apple iPhone 14", "Sony WH-1000XM5",
        "Dell Laptop 15", "Levi's Jeans", "Nike Running Shoes",
        "The Alchemist", "Atomic Habits", "LG 4K TV",
        "Instant Pot", "Adidas T-Shirt", "Kindle Paperwhite",
        "Canon DSLR Camera", "HP Printer", "Wooden Bookshelf",
        "Cotton Bedsheet Set", "Python Crash Course", "OnePlus Nord",
        "Air Purifier", "Kitchen Knife Set", "Table Lamp",
        "JBL Bluetooth Speaker"
    ],
    "category": [
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Clothing", "Clothing",
        "Books", "Books", "Electronics",
        "Home", "Clothing", "Electronics",
        "Electronics", "Electronics", "Home",
        "Home", "Books", "Electronics",
        "Home", "Home", "Home",
        "Electronics"
    ],
    "price": [
        79999, 69999, 29999,
        55000, 2999, 5499,
        299, 499, 49999,
        8999, 999, 14999,
        42000, 12000, 6500,
        1499, 599, 27999,
        9999, 2500, 1200,
        4999
    ],
    "stock": [
        120, 85, 200,
        50, 300, 180,
        500, 450, 60,
        95, 400, 140,
        40, 75, 30,
        200, 600, 110,
        65, 90, 150,
        250
    ],
    "rating": [
        4.5, 4.7, 4.6,
        4.2, 3.9, 4.4,
        4.8, 4.9, 4.3,
        4.1, 3.7, 4.6,
        4.5, 3.8, 4.0,
        3.5, 4.7, 4.3,
        4.2, 4.0, 3.6,
        4.4
    ],
    "num_reviews": [
        350, 520, 410,
        180, 95, 230,
        870, 1200, 145,
        310, 60, 480,
        200, 90, 55,
        140, 750, 300,
        125, 85, 70,
        390
    ]
}

df = pd.DataFrame(data)
print("=" * 55)
print("        E-COMMERCE PRODUCT ANALYZER")
print("=" * 55)

# -----------------------------------------------
# Step 2: 'First 5 Minutes' Checklist
# -----------------------------------------------
print("\n--- First 5 Minutes Checklist ---")

print(f"\n[1] Shape: {df.shape}  ({df.shape[0]} rows, {df.shape[1]} columns)")

print("\n[2] Column names:")
print(list(df.columns))

print("\n[3] Data types:")
print(df.dtypes)

print("\n[4] First 5 rows (df.head()):")
print(df.head())

print("\n[5] Basic stats (df.describe()):")
print(df.describe())

print("\n[6] Missing values:")
print(df.isnull().sum())

print("\n[7] df.info():")
df.info()

# -----------------------------------------------
# Step 3: .loc[] operations
# -----------------------------------------------
print("\n--- .loc[] Operations ---")

# (a) All Electronics products
electronics = df.loc[df["category"] == "Electronics"]
print(f"\n(a) Electronics products ({len(electronics)} items):")
print(electronics[["name", "price", "rating"]])

# (b) Products rated > 4.0 AND price < 5000
affordable_rated = df.loc[(df["rating"] > 4.0) & (df["price"] < 5000)]
print(f"\n(b) Rating > 4.0 and Price < 5000 ({len(affordable_rated)} items):")
print(affordable_rated[["name", "price", "rating"]])

# (c) Update stock for a specific product (The Alchemist)
idx = df.loc[df["name"] == "The Alchemist"].index[0]
df.loc[idx, "stock"] = 550
print(f"\n(c) Updated stock for 'The Alchemist': {df.loc[idx, 'stock']}")

# -----------------------------------------------
# Step 4: .iloc[] operations
# -----------------------------------------------
print("\n--- .iloc[] Operations ---")

# (a) First 5 and last 5 products
print("\n(a) First 5 products:")
print(df.iloc[:5][["name", "price"]])
print("\nLast 5 products:")
print(df.iloc[-5:][["name", "price"]])

# (b) Every other row
print("\n(b) Every other row:")
print(df.iloc[::2][["name", "category"]])

# (c) Rows 10-15, columns 0-3
print("\n(c) Rows 10-15, columns 0-3:")
print(df.iloc[10:16, 0:4])

# -----------------------------------------------
# Step 5: Create 3 filtered DataFrames
# -----------------------------------------------
budget_products = df.loc[df["price"] < 1000]
premium_products = df.loc[df["price"] > 10000]
popular_products = df.loc[(df["num_reviews"] > 100) & (df["rating"] > 4.0)]

print("\n--- Filtered DataFrames ---")
print(f"\nBudget Products (price < 1000): {len(budget_products)} items")
print(budget_products[["name", "price"]])

print(f"\nPremium Products (price > 10000): {len(premium_products)} items")
print(premium_products[["name", "price"]])

print(f"\nPopular Products (reviews > 100 and rating > 4.0): {len(popular_products)} items")
print(popular_products[["name", "num_reviews", "rating"]])

# -----------------------------------------------
# Step 6: Export each filtered DataFrame to CSV
# -----------------------------------------------
filtered_dfs = {
    "budget_products": budget_products,
    "premium_products": premium_products,
    "popular_products": popular_products
}

for filename, filtered_df in filtered_dfs.items():
    filepath = f"{filename}.csv"
    filtered_df.to_csv(filepath, index=False)
    print(f"\nExported: {filepath} ({len(filtered_df)} rows)")

print("\nDone!")
