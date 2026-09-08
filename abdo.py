import pandas as pd
import numpy as np

data = {
    "order_id": [1,2,3,4,5,6],
    "product": ["phone","laptop","phone","tablet","laptop","phone"],
    "price": [500,1200,np.nan,300,1200,500],
    "quantity": [2,1,3,np.nan,2,1],
    "date": ["2024-01-01","2024-01-05","2024-02-10","2024-02-15","2024-03-01","2024-03-10"]
}

df = pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.isnull().sum())
#########################################
df["price"].fillna(df["price"].mean(), inplace=True)
df["quantity"].fillna(1, inplace=True)
#########################################
df["total"] = df["price"] * df["quantity"]
#########################################
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
#########################################
product_sales = df.groupby("product")["total"].sum()
print(product_sales)

monthly_sales = df.groupby("month")["total"].sum()
print(monthly_sales)

#########################################
pivot = pd.pivot_table(
    df,
    values="total",
    index="product",
    aggfunc="sum"
)

print(pivot)
#########################################
print(df)