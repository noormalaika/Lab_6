
import pandas as pd
import matplotlib.pyplot as plt

# Create a product inventory dataset
data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Yogurt", "Water", "Cookies", "Cheese", "Energy Drink"
    ],
    "Category": [
        "beverages ", "SNACKS", " Dairy", "Snacks",
        "beverages", "DAIRY ", " Beverages", "snacks ",
        "dairy", "BEVERAGES"
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120",
        "Rs. 1,800", "Rs. 220", "Rs. 80", "Rs. 150",
        "Rs. 650", "Rs. 2,000"
    ],
    "Stock": [40, 120, 60, 100, 35, 75, 150, 80, 45, 25]
}

df = pd.DataFrame(data)

# Clean category names
df["Category"] = df["Category"].str.strip().str.title()

# Remove currency prefix and commas, then convert to numbers
df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Encode categories with numeric labels
df["Category_Code"] = df["Category"].astype("category").cat.codes

# Print the cleaned dataset
print("Cleaned Inventory Dataset:")
print(df.to_string(index=False))

# Calculate average price and total stock per category
average_price = df.groupby("Category")["Price"].mean()
category_stock = df.groupby("Category")["Stock"].sum()

# Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot of average price
average_price.plot(kind="bar", ax=axes[0])
axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=0)

# Pie chart of each category's share of total stock
axes[1].pie(
    category_stock,
    labels=category_stock.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1].set_title("Share of Total Stock")

plt.tight_layout()
plt.savefig("inventory_plots.png", dpi=300)
plt.show()

print("Saved inventory_plots.png")
