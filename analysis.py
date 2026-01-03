import pandas as pd

# Load the dataset
df = pd.read_csv("data/sales_data.csv")

# Show first rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())
# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

print("\nDate column converted to datetime")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nCleaned Dataset Preview:")
print(df.head())

# Total sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Product-wise sales
product_sales = df.groupby('Product')['Sales'].sum()
print("\nProduct-wise Sales:")
print(product_sales)

# Region-wise sales
region_sales = df.groupby('Region')['Sales'].sum()
print("\nRegion-wise Sales:")
print(region_sales)

# Category-wise sales
category_sales = df.groupby('Category')['Sales'].sum()
print("\nCategory-wise Sales:")
print(category_sales)



import matplotlib.pyplot as plt
# Product-wise sales bar chart
product_sales.plot(kind='bar')
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig("visuals/product_sales.png")
plt.show()

# Region-wise sales pie chart
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Region-wise Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visuals/region_sales.png")
plt.show()


# Monthly sales trend
df['Month'] = df['Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/monthly_sales.png")
plt.show()
