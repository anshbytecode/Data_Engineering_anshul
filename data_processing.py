import pandas as pd

df = pd.read_csv("../data/processed/sales_data_cleaned.csv")

daily_sales = df.groupby("Date")["TotalAmount"].sum().reset_index()

product_sales = df.groupby("ProductID")["TotalAmount"].sum().reset_index()

store_sales = df.groupby("StoreID")["TotalAmount"].sum().reset_index()

daily_sales.to_csv("../outputs/daily_sales.csv", index=False)
product_sales.to_csv("../outputs/product_sales.csv", index=False)
store_sales.to_csv("../outputs/store_sales.csv", index=False)

avg_order_value = df["TotalAmount"].mean()
total_revenue = df["TotalAmount"].sum()
unique_transactions = df["TransactionID"].nunique()

print("KPI Report:")
print(f"Total Revenue: {total_revenue}")
print(f"Average Order Value: {avg_order_value}")
print(f"Unique Transactions: {unique_transactions}")
