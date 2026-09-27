import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)



df = pd.read_csv('sales.csv')


print(df)

print(df.head())


print(df.tail())

print("Rows and Columns:", df.shape)


print(df.columns)
print(df.dtypes)

print(df.info())
print(df.describe())


print(df.isnull().sum())

print("Duplicate records:", df.duplicated().sum())


df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="mixed", dayfirst=True)

print(df)

print(df.dtypes)


df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.strftime("%B")
print(df)


df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

print(df)

total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)
total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)
total_quantity = df["Quantity"].sum()

print("Total Quantity:", total_quantity)
category_sales = df.groupby("Category")["Sales"].sum()



import os


os.makedirs("charts", exist_ok=True)


plt.savefig("charts/sales_by_category.png")



category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig("charts/sales_by_category.png")
plt.show()

print(category_sales)

category_profit = df.groupby("Category")["Profit"].sum()

print(category_profit)
city_sales = df.groupby("City")["Sales"].sum()

print(city_sales)

city_profit = df.groupby("City")["Profit"].sum()

print(city_profit)

product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales.sort_values(ascending=False))

highest_sales = df.loc[df["Sales"].idxmax()]

print(highest_sales)

highest_profit = df.loc[df["Profit"].idxmax()]

print(highest_profit)

monthly_sales = df.groupby("Month_Name")["Sales"].sum()

print(monthly_sales)


city_sales = df.groupby("City")["Sales"].sum()

city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig("charts/sales_by_city.png")
plt.show()


daily_sales = df.groupby("Order_Date")["Sales"].sum()

daily_sales.plot(kind="line")

plt.title("Sales Trend")
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/sales_trend.png")
plt.show()


category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales Distribution by Category")
plt.ylabel("")

plt.savefig("charts/category_sales_pie.png")
plt.show()


category_profit = df.groupby("Category")["Profit"].sum()

category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("charts/profit_by_category.png")
plt.show()



import os


os.makedirs("output", exist_ok=True)


df.to_csv("output/cleaned_sales.csv", index=False)


