import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Fix date issue
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')

# Create Month column
df['Month'] = df['Order Date'].dt.to_period('M')

# 📊 Sales Trend
sales_trend = df.groupby('Month')['Sales'].sum()
sales_trend.plot()
plt.title("Sales Trend")
plt.savefig("sales_trend.png")
plt.show()

# 🛍️ Top Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar')
plt.title("Top Products")
plt.savefig("top_products.png")
plt.show()

# 🏷️ Category
category = df.groupby('Category')['Profit'].sum()
category.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Profit")
plt.savefig("category.png")
plt.show()

# 🌍 Region
region = df.groupby('Region')['Sales'].sum()
region.plot(kind='bar')
plt.title("Region Sales")
plt.savefig("region.png")
plt.show()
