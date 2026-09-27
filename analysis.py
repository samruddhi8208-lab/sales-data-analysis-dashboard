import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# Create output folders
os.makedirs("charts", exist_ok=True)
os.makedirs("output", exist_ok=True)

# Read sales data
df = pd.read_csv("sales.csv")

print("========== DATA ==========")
print(df)

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== LAST 5 ROWS ==========")
print(df.tail())

print("\nRows and Columns:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nData Info:")
df.info()

print("\nStatistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())


# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    format="mixed",
    dayfirst=True
)

print("\n========== CONVERTED DATA ==========")
print(df)

print("\nUpdated Data Types:")
print(df.dtypes)


# Create Month columns
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.strftime("%B")

# Calculate Profit Margin
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

print("\n========== PROCESSED DATA ==========")
print(df)


# =========================
# SUMMARY
# =========================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

print("\n========== SUMMARY ==========")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Quantity:", total_quantity)


# =========================
# CATEGORY ANALYSIS
# =========================

category_sales = df.groupby("Category")["Sales"].sum()

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)

category_profit = df.groupby("Category")["Profit"].sum()

print("\n========== PROFIT BY CATEGORY ==========")
print(category_profit)


# Sales by Category Chart
plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig("charts/sales_by_category.png")
plt.close()


# Profit by Category Chart
plt.figure(figsize=(8, 5))

category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()

plt.savefig("charts/profit_by_category.png")
plt.close()


# Category Pie Chart
plt.figure(figsize=(7, 7))

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales Distribution by Category")
plt.ylabel("")

plt.tight_layout()
plt.savefig("charts/category_sales_pie.png")
plt.close()


# =========================
# CITY ANALYSIS
# =========================

city_sales = df.groupby("City")["Sales"].sum()

print("\n========== SALES BY CITY ==========")
print(city_sales)

city_profit = df.groupby("City")["Profit"].sum()

print("\n========== PROFIT BY CITY ==========")
print(city_profit)


# Sales by City Chart
plt.figure(figsize=(10, 6))

city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/sales_by_city.png")
plt.close()


# =========================
# PRODUCT ANALYSIS
# =========================

product_sales = df.groupby("Product")["Sales"].sum()

print("\n========== SALES BY PRODUCT ==========")
print(product_sales.sort_values(ascending=False))


# Highest Sales Transaction
highest_sales = df.loc[df["Sales"].idxmax()]

print("\n========== HIGHEST SALES ==========")
print(highest_sales)


# Highest Profit Transaction
highest_profit = df.loc[df["Profit"].idxmax()]

print("\n========== HIGHEST PROFIT ==========")
print(highest_profit)


# =========================
# MONTHLY / DAILY ANALYSIS
# =========================

monthly_sales = df.groupby("Month_Name")["Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)


daily_sales = df.groupby("Order_Date")["Sales"].sum()


# Sales Trend Chart
plt.figure(figsize=(12, 6))

daily_sales.plot(kind="line")

plt.title("Sales Trend")
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/sales_trend.png")
plt.close()


# =========================
# SAVE CLEANED DATA
# =========================

df.to_csv(
    "output/cleaned_sales.csv",
    index=False
)

print("\n========== COMPLETED ==========")
print("Charts saved in: charts/")
print("Cleaned data saved in: output/cleaned_sales.csv")
