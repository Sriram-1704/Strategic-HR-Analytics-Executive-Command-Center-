import pandas as pd
import numpy as np

# Loading Dataset
df = pd.read_csv("Data/Raw/HR_Analytics_Raw_Dataset.csv")
print("Dataset Shape Before Cleaning:", df.shape)

# Removing Irrelevant Columns
columns_to_drop = [
    "EmployeeCount",
    "Over18",
    "StandardHours"
]
df.drop(columns=columns_to_drop, inplace=True)

# Check Data Types
print("\nData Types:")
print(df.dtypes)

# Convert Age to Numeric
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

# Convert YearsAtCompany to Numeric
df["YearsAtCompany"] = pd.to_numeric(
    df["YearsAtCompany"],
    errors="coerce"
)

# Handle Missing Values

# Numerical Columns
numerical_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns
for col in numerical_columns:
    df[col].fillna(
        df[col].median(),
        inplace=True
    )

# Categorical Columns
categorical_columns = df.select_dtypes(
    include=["object"]
).columns
for col in categorical_columns:
    df[col].fillna(
        df[col].mode()[0],
        inplace=True
    )

# Clean Department Values
df["Department"] = df["Department"].str.strip()
df["Department"] = df["Department"].replace({
    "Sales Dept": "Sales",
    "Sales Department": "Sales",
    "sales": "Sales",
    "HR": "Human Resources",
    "Human Resource": "Human Resources",
    "human resources": "Human Resources",
    "R&D": "Research & Development",
    "R & D": "Research & Development",
    "Research Dept": "Research & Development",
    "Research and Development": "Research & Development"
})

# Clean JobRole Values
df["JobRole"] = df["JobRole"].str.strip()

# Clean Gender Values
df["Gender"] = df["Gender"].str.strip()

# Clean Marital Status Values
df["MaritalStatus"] = df["MaritalStatus"].str.strip()

# Encoding Attrition Yes = 1, No = 0
df["Attrition"] = df["Attrition"].map(
    {
        "Yes": 1,
        "No": 0
    }
)

# Checking Duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate Records:")
print(duplicates)

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Verify Department Values
print("\nDepartment Counts:")
print(df["Department"].value_counts())

# Verify Job Roles
print("\nSample Job Roles:")
print(df["JobRole"].value_counts().head())

# Dataset Shape After Cleaning
print("\nDataset Shape After Cleaning:")
print(df.shape)

# Saving File
df.to_csv(
    "Data/Cleaned/HR_Analytics_Cleaned.csv",
    index=False
)
