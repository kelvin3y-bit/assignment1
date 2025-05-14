import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris


try:
    # Load the dataset
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = iris_data.target
    df['species'] = df['species'].map(dict(zip(range(3), iris_data.target_names)))

    # Display first few rows
    print("First 5 rows:")
    print(df.head())

    # Dataset structure
    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

except Exception as e:
    print("Error loading dataset:", e)

# dropping missing values i
df.dropna(inplace=True)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species and compute mean
print("\nMean values by species:")
print(df.groupby('species').mean())

# Interesting pattern: Petal length differences
print("\nObservation:")
print("Setosa species generally has shorter petal lengths compared to others.")

# Simulate a 'day' column for line chart
df['day'] = pd.date_range(start='2024-01-01', periods=len(df), freq='D')

plt.figure(figsize=(10,5))
plt.plot(df['day'], df['sepal length (cm)'], label='Sepal Length')
plt.title("Sepal Length Over Time")
plt.xlabel("Date")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.grid(True)
plt.show()

#petal length distribution barplot
species_avg = df.groupby('species')['petal length (cm)'].mean().reset_index()

plt.figure(figsize=(8,6))
sns.barplot(data=species_avg, x='species', y='petal length (cm)', palette='viridis')
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

#width distribution histogram
plt.figure(figsize=(8,6))
plt.hist(df['sepal width (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot of sepal length vs width
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='deep')
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()

