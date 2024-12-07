import pandas as pd

# Load the dataset
data = pd.read_csv("index.csv")

# Display the first few rows
print(data.head())

#Check for missing values
print(data.isnull().sum())

# Fill missing values
data['card'].fillna('Unknown', inplace=True)  # Assuming 'card' can be unknown
data['money'].fillna(data['money'].median(), inplace=True)  # Fill with median

# Convert date columns to datetime
data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y')
data['datetime'] = pd.to_datetime(data['datetime'])

# Check for duplicates
data.drop_duplicates(inplace=True)

import matplotlib.pyplot as plt
import seaborn as sns

# Sales by coffee type
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='coffee_name', order=data['coffee_name'].value_counts().index)
plt.title('Sales by Coffee Type')
plt.xticks(rotation=45)
plt.show()

# Group by date and sum the money
daily_sales = data.groupby('date')['money'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_sales, x='date', y='money')
plt.title('Daily Sales Trend')
plt.xticks(rotation=45)
plt.show()

data['hour'] = data['datetime'].dt.hour  # Extract hour from datetime

# Group by hour and sum the sales
hourly_sales = data.groupby('hour')['money'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=hourly_sales, x='hour', y='money')
plt.title('Sales by Hour of the Day')
plt.xticks(rotation=0)
plt.show()

# Save cleaned data to a new CSV file
data.to_csv('cleaned_coffee_sales.csv', index=False)