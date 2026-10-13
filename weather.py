
import pandas as pd
import matplotlib.pyplot as plt

# Create a messy 15-day weather dataset
data = {
    "Date": [
        "2026-09-01", "2026-09-02", "2026-09-03",
        "2026-09-04", "2026-09-05", "2026-09-06",
        "2026-09-07", "2026-09-08", "2026-09-09",
        "2026-09-10", "2026-09-11", "2026-09-12",
        "2026-09-13", "2026-09-14", "2026-09-15",
        "2026-09-01"
    ],
    "City": [
        " islamabad", "ISLAMABAD ", "lahore", " Lahore ",
        "KARACHI", "karachi ", " Islamabad ", "LAHORE",
        "karachi", " ISLAMABAD", "lahore ", "KARACHI ",
        "Islamabad", " LAHORE", "karachi", " islamabad"
    ],
    "Temperature": [
        "32C", "30C", "35C", "29C", "34C",
        "31C", "33C", "28C", "36C", "31C",
        "30C", "33C", "34C", "29C", "35C", "32C"
    ],
    "Humidity": [
        45, 50, None, 65, 40, 55, 48, None,
        38, 60, 58, None, 42, 68, 35, 45
    ],
    "Condition": [
        "sunny", " CLOUDY ", "Sunny", " Rainy",
        "SUNNY ", "cloudy", " sunny", "CLOUDY",
        "Rainy ", "Sunny", " cloudy ", "RAINY",
        "SUNNY", "cloudy", " Sunny ", " SUNNY"
    ]
}

df = pd.DataFrame(data)

# Clean text columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# Remove the temperature unit and convert to numeric
df["Temperature"] = (
    df["Temperature"].str.replace("C", "", regex=False).astype(float)
)

# Convert Date strings into datetime values
df["Date"] = pd.to_datetime(df["Date"])

# Remove duplicate rows
df = df.drop_duplicates().copy()
print("Rows after dropping duplicates:", len(df))

# Fill missing humidity with the median
humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)

print("Missing Humidity filled with median:", humidity_median)

# One-hot encode the Condition column
condition_encoded = pd.get_dummies(
    df["Condition"], prefix="Condition", dtype=int
)

print("\nOne-hot encoded Condition columns:")
print(condition_encoded.to_string(index=False))

# Calculate and print the correlation
correlation = df["Temperature"].corr(df["Humidity"])
print("\nCorrelation (Temperature, Humidity):", round(correlation, 2))

# Print condition counts
condition_counts = df["Condition"].value_counts()
print("\nCondition counts:")
print(condition_counts)

# Create a 2 x 2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# 1. Line plot: Temperature over Date
axes[0, 0].plot(
    df["Date"], df["Temperature"], marker="o"
)
axes[0, 0].set_title("Temperature Over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Scatter plot: Temperature vs Humidity
axes[0, 1].scatter(df["Temperature"], df["Humidity"])
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity")

# 3. Pie chart: Weather conditions
axes[1, 0].pie(
    condition_counts,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Weather Condition Distribution")

# 4. Histogram: Temperature
axes[1, 1].hist(df["Temperature"], bins=6, edgecolor="black")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

# Add the overall title and save the dashboard
fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("weather_dashboard.png", dpi=300)
plt.show()

print("\nSaved weather_dashboard.png")
