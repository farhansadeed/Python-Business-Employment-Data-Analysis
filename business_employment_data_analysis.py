
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('business-employment-data-march-2023-quarter-industry-revisions.csv')

# 1. Line plot showing the trend of filled jobs (both original and revised) across different quarters for each industry
plt.figure(figsize=(14, 8))
sns.lineplot(x='quarter', y='filled jobs', hue='industry_name', data=data, marker='o', label='Original')
sns.lineplot(x='quarter', y='filled jobs revised', hue='industry_name', data=data, marker='x', label='Revised', linestyle='--')
plt.title('Trend of Filled Jobs (Original and Revised) Across Quarters by Industry')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.ylabel('Filled Jobs')
plt.xlabel('Quarter')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar plot highlighting the percentage difference in filled jobs and earnings for each industry in December 2022
dec_2022_data = data[data['quarter'] == 2022.12]
plt.figure(figsize=(14, 8))
sns.barplot(x='industry_name', y='filled jobs % diff', data=dec_2022_data, color='blue', label='Filled Jobs % Diff')
sns.barplot(x='industry_name', y='earnings % diff', data=dec_2022_data, color='orange', label='Earnings % Diff', alpha=0.6)
plt.title('Percentage Difference in Filled Jobs and Earnings by Industry (December 2022)')
plt.legend()
plt.ylabel('Percentage Difference (%)')
plt.xlabel('Industry Name')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Heatmap showing the percentage difference in filled jobs across industries and quarters
heatmap_data = data.pivot_table(index='industry_name', columns='quarter', values='filled jobs % diff')
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, cmap='RdYlGn', annot=True, linewidths=.5, cbar_kws={'label': 'Percentage Difference (%)'})
plt.title('Heatmap of Percentage Difference in Filled Jobs Across Industries and Quarters')
plt.ylabel('Industry Name')
plt.xlabel('Quarter')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

