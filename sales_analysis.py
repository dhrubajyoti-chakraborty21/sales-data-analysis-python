import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Basic analysis
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

# Sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print(sales_by_product)

# Visualization
sales_by_product.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()
