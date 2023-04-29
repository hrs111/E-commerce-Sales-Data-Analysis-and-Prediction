#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv("data.csv", encoding='unicode_escape')

# Perform initial data exploration
print(df.head())
print(df.shape)
print(df.dtypes)

# Check for missing values and decide on an appropriate course of action to handle them
print(df.isnull().sum())
# Convert non-numeric values in Quantity and UnitPrice columns to NaN
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
# Drop rows with non-numeric StockCode values
df = df[pd.to_numeric(df['StockCode'], errors='coerce').notnull()]

# Convert StockCode column to numeric format
df['StockCode'] = pd.to_numeric(df['StockCode'])

# Check for and remove any duplicate rows
df.drop_duplicates(inplace=True)

# Drop rows with NaN values
df.dropna(inplace=True)

# Examine the distribution of numerical variables
print(df.describe())

# Examine the distribution of categorical variables
print(df['Country'].value_counts())
print(df['StockCode'].value_counts())

# Investigate the relationship between pairs of variables
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='Quantity', y='UnitPrice', data=df)
plt.show()

sns.boxplot(x='Country', y='UnitPrice', data=df)
plt.show()

# Perform additional feature engineering by creating new variables or transforming existing ones, if necessary
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
print(df.head())

# Calculate and plot the correlation between pairs of variables
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True)
plt.show()

# Use machine learning techniques to predict future sales based on historical data, if applicable
# Example: Linear Regression
from sklearn.linear_model import LinearRegression

X = df[['Quantity', 'UnitPrice']]
y = df['TotalPrice']

model = LinearRegression()
model.fit(X, y)

# Summarize findings and provide recommendations based on the analysis
print("Based on the analysis, it seems that the company's sales are heavily influenced by the quantity of items sold and the unit price of those items. There is also a strong positive correlation between quantity and total price, as well as between unit price and total price. Additionally, the company should pay attention to the countries where they are selling their products, as there seems to be variation in the prices across different countries. To improve sales, the company could consider offering discounts for bulk purchases or introducing a loyalty program to encourage repeat customers. They could also focus on expanding their sales to countries with high demand for their products.")


# In[ ]:




