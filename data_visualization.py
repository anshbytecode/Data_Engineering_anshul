import pandas as pd
import matplotlib.pyplot as plt

daily_sales = pd.read_csv("../outputs/daily_sales.csv")
product_sales = pd.read_csv("../outputs/product_sales.csv")
store_sales = pd.read_csv("../outputs/store_sales.csv")

plt.figure(figsize=(10,5))
plt.plot(daily_sales["Date"], daily_sales["TotalAmount"])
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.savefig("../outputs/sales_trend.png")

top_products = product_sales.sort_values(by="TotalAmount", ascending=False).head(5)
plt.figure(figsize=(8,5))
plt.bar(top_products["ProductID"], top_products["TotalAmount"])
plt.title("Top 5 Products by Revenue")
plt.savefig("../outputs/top_products.png")

plt.figure(figsize=(8,5))
plt.bar(store_sales["StoreID"], store_sales["TotalAmount"])
plt.title("Store-wise Sales Comparison")
plt.savefig("../outputs/store_comparison.png")
