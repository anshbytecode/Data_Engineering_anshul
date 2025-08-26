import pandas as pd

df = pd.read_csv("../data/raw/sales_data.csv")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(float)
df['TotalAmount'] = df['Quantity'] * df['Price']

df.to_csv("../data/processed/sales_data_cleaned.csv", index=False)
print("Data cleaning completed & saved.")
