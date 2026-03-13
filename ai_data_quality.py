"""
Part D: AI-Augmented Task
Prompt used, AI output, testing on 2 DataFrames, and critical evaluation.
"""

import pandas as pd
import numpy as np

# -----------------------------------------------
# Prompt I used:
# "Write a Python function that takes a Pandas DataFrame and generates an
#  automated data quality report including: shape, dtypes, missing values
#  percentage, duplicate rows, unique value counts per column, and basic
#  stats. Return the report as a dict and also print a formatted summary."
# -----------------------------------------------

# -----------------------------------------------
# AI Output (tested and slightly cleaned up):
# -----------------------------------------------
def data_quality_report(df):
    """
    Generates an automated data quality report for the given DataFrame.
    Returns a dict and prints a formatted summary.
    """
    if df.empty:
        print("DataFrame is empty. No report generated.")
        return {}

    report = {}

    # Shape
    report["shape"] = {"rows": df.shape[0], "cols": df.shape[1]}

    # Data types
    report["dtypes"] = df.dtypes.astype(str).to_dict()

    # Missing values percentage per column
    missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
    report["missing_pct"] = missing_pct.to_dict()

    # Duplicate rows
    report["duplicate_rows"] = int(df.duplicated().sum())

    # Unique value counts per column
    report["unique_counts"] = {col: int(df[col].nunique()) for col in df.columns}

    # Columns with only 1 unique value (useless features)
    report["single_value_cols"] = [
        col for col in df.columns if df[col].nunique() == 1
    ]

    # Basic stats for numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        report["basic_stats"] = numeric_df.describe().round(2).to_dict()
    else:
        report["basic_stats"] = {}

    # Memory usage in MB
    report["memory_mb"] = round(df.memory_usage(deep=True).sum() / (1024 ** 2), 4)

    # --- Print Formatted Summary ---
    print("=" * 50)
    print("        DATA QUALITY REPORT")
    print("=" * 50)
    print(f"  Rows            : {report['shape']['rows']}")
    print(f"  Columns         : {report['shape']['cols']}")
    print(f"  Duplicate Rows  : {report['duplicate_rows']}")
    print(f"  Memory Usage    : {report['memory_mb']} MB")

    print("\n  Missing Values (%):")
    for col, pct in report["missing_pct"].items():
        flag = " ⚠" if pct > 0 else ""
        print(f"    {col:25s}: {pct}%{flag}")

    print("\n  Unique Value Counts:")
    for col, cnt in report["unique_counts"].items():
        print(f"    {col:25s}: {cnt}")

    if report["single_value_cols"]:
        print(f"\n  ⚠ Single-value columns (useless features): {report['single_value_cols']}")
    else:
        print("\n  No single-value columns found.")

    return report


# -----------------------------------------------
# Test 1: Clean DataFrame
# -----------------------------------------------
print("\n\n### TEST 1: Clean DataFrame ###\n")
clean_df = pd.DataFrame({
    "product_id": range(1, 11),
    "name": [f"Product_{i}" for i in range(1, 11)],
    "price": [499, 999, 1999, 299, 799, 599, 1299, 399, 899, 2499],
    "rating": [4.1, 4.5, 3.8, 4.7, 4.0, 3.5, 4.8, 4.2, 3.9, 4.6],
    "in_stock": [True]*10
})

report1 = data_quality_report(clean_df)

# -----------------------------------------------
# Test 2: Messy DataFrame (missing values, duplicates, useless column)
# -----------------------------------------------
print("\n\n### TEST 2: Messy DataFrame ###\n")
messy_df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 3, 7, 8],          # has a duplicate (id=3)
    "name": ["Alice", "Bob", None, "Diana", "Eve", "Charlie", None, "Hank"],
    "age": [25, None, 35, None, 28, 35, 40, None],
    "salary": [50000, 60000, 70000, None, 55000, 70000, 80000, 45000],
    "country": ["India"] * 8      # single-value column (useless feature)
})

report2 = data_quality_report(messy_df)


# -----------------------------------------------
# Critical Evaluation (Q4 written answer)
# -----------------------------------------------
print("""

==============================================
  CRITICAL EVALUATION OF AI-GENERATED CODE
==============================================

The AI-generated function handled most common cases well. It correctly
computes shape, dtypes, missing value percentages, duplicate counts, unique
values, and basic stats. Using df.memory_usage(deep=True) is the right
approach for accurate memory reporting.

However, I noticed a few gaps:

1. Edge case - empty DataFrame: The original AI output didn't check if the
   DataFrame was empty before running operations. This would throw errors on
   describe() and other calls. I added an early check for df.empty.

2. Single-value columns: The AI didn't include detection of useless features
   (columns with only one unique value). I added that check since it's very
   useful in real data cleaning workflows.

3. All-null columns: If a column is 100% null, the describe() output won't
   include it in numeric stats. The function handles this gracefully by
   using select_dtypes first, but a clearer warning for fully-null columns
   would help.

4. Categorical columns: The function doesn't report the most frequent value
   (mode) for object/categorical columns - that would be a useful addition.

5. Data type assumptions: The function uses np.number to detect numeric
   columns, which won't catch bool columns. A minor improvement would be to
   handle boolean types separately.

Overall the AI output was a solid starting point. With the 5 improvements
above, it becomes production-ready.
""")
