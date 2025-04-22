# Objective 2

"""
Evaluate ROI based on Budget and Revenue
Goal: Calculate ROI from Budget and Revenue_Generated to assess campaign profitability.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("datapython.csv")

# Calculate ROI
df['ROI_Calculated'] = (df['Revenue_Generated'] - df['Budget']) / df['Budget'] * 100

# Plot ROI distribution
sns.histplot(df['ROI_Calculated'], bins=30, kde=True)
plt.title("Distribution of ROI (%)")
plt.xlabel("ROI (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
