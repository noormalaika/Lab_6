
import pandas as pd
import matplotlib.pyplot as plt

# Create the student marks dataset
data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA",
             "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

# Clean student names
df["Name"] = df["Name"].str.strip().str.title()

# Convert marks into numeric values
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Replace the missing mark with the mean of the other marks
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

# Print the cleaned DataFrame
print("Cleaned Student Marks Dataset:")
print(df)

# Create a bar plot
plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()

# Save the plot
plt.savefig("marks_bar.png", dpi=300)
plt.show()

print("Saved marks_bar.png")
