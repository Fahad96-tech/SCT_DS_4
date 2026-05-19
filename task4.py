import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales4_csv.csv", encoding="latin1")

print("\nDataset Preview:")
print(df.head())

print("\nColumns:")
print(df.columns)

df.dropna(inplace=True)

sns.set_style("whitegrid")

plt.figure(figsize=(10,5))
sns.countplot(x='Category', data=df)
plt.title("Products by Category")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(x='Region', data=df)
plt.title("Sales by Region")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(df['Sales'], bins=30, kde=True)
plt.title("Sales Distribution")
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(df['Profit'], bins=30, kde=True)
plt.title("Profit Distribution")
plt.show()

plt.figure(figsize=(10,5))
sns.scatterplot(x='Sales', y='Profit', data=df)
plt.title("Sales vs Profit")
plt.show()

plt.figure(figsize=(12,8))

numeric_df = df.select_dtypes(include=['number'])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

print("\nSummary Insights")

print("\nTop Category:")
print(df['Category'].value_counts().head(1))

print("\nTop Region:")
print(df['Region'].value_counts().head(1))

print("\nHighest Sales:")
print(df['Sales'].max())

print("\nHighest Profit:")
print(df['Profit'].max())