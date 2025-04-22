# Objective 4

"""
Analyze Flash Sale Impact on Units Sold
Goal: Understand how Flash Sales with varying discount levels affect the total number of units sold.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("datapython.csv")

# Group by Flash Sale and calculate average units sold
flash_sale_units = df.groupby('Flash_Sale_ID')['Units_Sold'].mean().reset_index()

# Bar plot
sns.barplot(data=flash_sale_units, x='Flash_Sale_ID', y='Units_Sold', palette='viridis')
plt.title("Average Units Sold per Flash Sale")
plt.xlabel("Flash Sale ID")
plt.ylabel("Average Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
