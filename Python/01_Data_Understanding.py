import pandas as pd
import numpy as np

# Loading Dataset

df = pd.read_csv("Data/Raw/HR_Analytics_Raw_Dataset.csv")

# First 5 Rows

print("\nFirst 5 Rows:")
print(df.head())

# Shape

print("\nDataset Shape:")
print(df.shape)

# Column Names

print("\nColumn Names:")
print(df.columns.tolist())

# Data Types

print("\nData Types:")
print(df.dtypes)

# Dataset Info

print("\nDataset Information:")
df.info()

# Statistical Summary

print("\nStatistical Summary:")
print(df.describe())

# Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# Missing Percentage

print("\nMissing Value Percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage.sort_values(ascending=False))

# Duplicate Records

print("\nDuplicate Records:")
print(df.duplicated().sum())

# Attrition Count

print("\nAttrition Count:")
print(df["Attrition"].value_counts())

# Attrition Percentage

print("\nAttrition Percentage:")
print(
    round(
        df["Attrition"].value_counts(normalize=True) * 100,
        2
    )
)

# Department Distribution

print("\nDepartment Distribution:")
print(df["Department"].value_counts())

# Gender Distribution

print("\nGender Distribution:")
print(df["Gender"].value_counts())

# Job Role Distribution

print("\nJob Role Distribution:")
print(df["JobRole"].value_counts())

# Business Travel Distribution

print("\nBusiness Travel Distribution:")
print(df["BusinessTravel"].value_counts())

# Marital Status Distribution

print("\nMarital Status Distribution:")
print(df["MaritalStatus"].value_counts())

# OverTime Distribution

print("\nOverTime Distribution:")
print(df["OverTime"].value_counts())

# Numerical Columns

print("\nNumerical Columns:")
numerical_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns

print(numerical_columns)

# Categorical Columns

print("\nCategorical Columns:")
categorical_columns = df.select_dtypes(
    include=["object"]
).columns

print(categorical_columns)

# Constant Columns

print("\nConstant Columns:")

for col in df.columns:
    if df[col].nunique() == 1:
        print(col)

# Total Missing Values

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())