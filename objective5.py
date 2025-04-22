# Objective 5

"""
Keyword Analysis in Campaigns
Goal: Identify the most common keywords used in campaigns to understand focus areas.
"""

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("datapython.csv")

# Combine all keywords into a single list
all_keywords = df['Common_Keywords'].dropna().str.cat(sep=',').split(',')

# Clean whitespace and count
keyword_counts = Counter([kw.strip().lower() for kw in all_keywords])

# Convert to DataFrame for plotting
keywords_df = pd.DataFrame(keyword_counts.items(), columns=['Keyword', 'Count'])
keywords_df = keywords_df.sort_values(by='Count', ascending=False).head(10)

# Plot
plt.figure(figsize=(10, 5))
plt.barh(keywords_df['Keyword'], keywords_df['Count'], color='skyblue')
plt.gca().invert_yaxis()
plt.title("Top 10 Campaign Keywords")
plt.xlabel("Frequency")
plt.tight_layout()
plt.show()
