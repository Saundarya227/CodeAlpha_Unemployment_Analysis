import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the unemployment dataset
df = pd.read_csv("Unemployment in India.csv")

# Display the first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check the number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Generate statistical summary
print("\nStatistical Summary:")
print(df.describe())




# DATA CLEANING

df.dropna(how="all", inplace=True)

df.columns = df.columns.str.strip()

df["Date"] = pd.to_datetime(
    df["Date"].str.strip(),
    format="%d-%m-%Y"
)

df.reset_index(drop=True, inplace=True)

print("\nCleaned Dataset Information:")
print(df.info())

print("\nCleaned Dataset Shape:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ANALYSIS 1: Unemployment Rate Over Time

# Calculate average unemployment rate for each date
monthly_unemployment = df.groupby("Date")[
    "Estimated Unemployment Rate (%)"
].mean()

# Create line graph
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_unemployment.index,
    monthly_unemployment.values,
    marker="o"
)

plt.title("Unemployment Rate Over Time in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save graph
plt.savefig("unemployment_trend.png", dpi=300)

plt.show()

# ANALYSIS 2: Rural vs Urban Unemployment

area_unemployment = df.groupby("Area")[
    "Estimated Unemployment Rate (%)"
].mean()

print("\nAverage Unemployment Rate by Area:")
print(area_unemployment)

# Create bar chart
plt.figure(figsize=(8, 5))

area_unemployment.plot(kind="bar")

plt.title("Average Unemployment Rate: Rural vs Urban")
plt.xlabel("Area")
plt.ylabel("Average Unemployment Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("rural_vs_urban.png", dpi=300)

plt.show()

# ANALYSIS 3: Top 10 States with Highest Unemployment Rate

# Calculate average unemployment rate for each state
state_unemployment = df.groupby("Region")[
    "Estimated Unemployment Rate (%)"
].mean()

# Sort in descending order and select top 10
top_10_states = state_unemployment.sort_values(
    ascending=False
).head(10)

print("\nTop 10 States with Highest Unemployment Rate:")
print(top_10_states)

# Create bar graph
plt.figure(figsize=(12, 6))

top_10_states.plot(kind="bar")

plt.title("Top 10 States with Highest Unemployment Rate")
plt.xlabel("States")
plt.ylabel("Average Unemployment Rate (%)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_10_states_unemployment.png", dpi=300)

plt.show()

# ANALYSIS 4: COVID-19 Period Comparison

rate_column = "Estimated Unemployment Rate (%)"

# Calculate average unemployment before April 2020
before_covid = df[df["Date"] < "2020-04-01"][rate_column].mean()

# Calculate average unemployment from April 2020 onwards
during_covid = df[df["Date"] >= "2020-04-01"][rate_column].mean()

# Store results
covid_comparison = pd.Series({
    "Before April 2020": before_covid,
    "April 2020 Onwards": during_covid
})

print("\nCOVID-19 Period Comparison:")
print(covid_comparison)

# Create bar chart
plt.figure(figsize=(8, 5))

covid_comparison.plot(kind="bar")

plt.title("Unemployment Rate: Before and During COVID-19 Period")
plt.xlabel("Period")
plt.ylabel("Average Unemployment Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("covid_impact.png", dpi=300)

plt.show()

# Loading the second dataset

df2 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

print("\nSecond Dataset Preview:")
print(df2.head())

print("\nSecond Dataset Information:")
print(df2.info())

print("\nSecond Dataset Shape:")
print(df2.shape)

# Unemployment Rate by Geographical Region

df2.columns = df2.columns.str.strip()

region_unemployment = df2.groupby("Region.1")[
    "Estimated Unemployment Rate (%)"
].mean().sort_values(ascending=False)

print("\nAverage Unemployment Rate by Geographical Region:")
print(region_unemployment)

plt.figure(figsize=(9, 5))
region_unemployment.plot(kind="bar")

plt.title("Average Unemployment Rate by Geographical Region")
plt.xlabel("Geographical Region")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("geographical_region_unemployment.png", dpi=300)
plt.show()