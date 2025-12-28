import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
categories = {
    "Laptop": "Electronics",
    "Mouse": "Accessories",
    "Keyboard": "Accessories",
    "Monitor": "Electronics",
    "Headphones": "Accessories"
}

region = ["North", "South", "East", "West"]

#data range ( 6 month data)
dates = pd.date_range(start='2024-01-01', end='2024-06-30')

data = {
    "Date": np.random.choice(dates, rows),
    "Product": np.random.choice(products, rows),
    "Region": np.random.choice(region, rows),
    "Quantity": np.random.randint(1, 6, rows),
    "UnitPrice": np.random.randint(500, 60000, rows)
}

df = pd.DataFrame(data)

#Category column
df["Category"] = df["Product"].map(categories)

#Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

#Month for Dashboard
df["Month"] = df["Date"].dt.to_period("M").astype(str)

print(df.head())
print("Rows and Columns : ", df.shape)  # use df.shape to quickly verify the size of the dataset.

#Export for EXCEL and Power BI
df.to_excel("Sales_Data.xlsx", index=False)
print("Data Exported")



# Generated a realistic company-level sales dataset with 1000 records using Python and NumPy, 
# including date, product, region, and revenue. 
# used this data to build a Power BI sales performance dashboard
