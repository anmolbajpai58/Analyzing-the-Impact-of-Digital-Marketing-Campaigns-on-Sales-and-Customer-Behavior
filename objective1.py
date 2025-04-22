# Objective 1

"""
Analyze the impact of Discount Levels on Units Sold
Goal: We want to understand if there's a pattern between the Discount_Level and the Units_Sold,
and whether higher discounts result in more units being sold.
"""

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load the dataset
df = pd.read_csv("datapython.csv")

# Preview the dataset
print(df.head())

# Create a boxplot for Discount_Level vs Units_Sold
sns.boxplot(data=df, x='Discount_Level', y='Units_Sold')
plt.title("Units Sold by Discount Level")
plt.xlabel("Discount Level")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()
