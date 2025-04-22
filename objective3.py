# Objective 3

"""
Analyze relationship between Subscription Length and Customer Satisfaction
Goal: Determine if longer subscriptions are correlated with higher customer satisfaction after refunds.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("datapython.csv")

# Scatter plot for Subscription_Length vs Customer_Satisfaction_Post_Refund
sns.scatterplot(data=df, x='Subscription_Length', y='Customer_Satisfaction_Post_Refund')
plt.title("Customer Satisfaction vs Subscription Length")
plt.xlabel("Subscription Length (months)")
plt.ylabel("Satisfaction Score")
plt.tight_layout()
plt.show()
