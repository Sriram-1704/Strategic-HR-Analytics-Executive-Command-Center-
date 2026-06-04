import pandas as pd

# Load Dataset
df = pd.read_csv("Data/Cleaned/HR_Analytics_Cleaned.csv")

print("Dataset Shape:", df.shape)

# Age Group
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[18, 25, 35, 45, 55, 65],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56-65"
    ]
)

# Income Group
df["IncomeGroup"] = pd.cut(
    df["MonthlyIncome"],
    bins=[0, 5000, 10000, 15000, 20000, 50000],
    labels=[
        "Low",
        "Medium",
        "High",
        "Very High",
        "Executive"
    ]
)

# Tenure Group
df["TenureGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[0, 2, 5, 10, 20, 50],
    labels=[
        "0-2 Years",
        "3-5 Years",
        "6-10 Years",
        "11-20 Years",
        "20+ Years"
    ]
)

# Attrition Label
df["AttritionLabel"] = df["Attrition"].map(
    {
        0: "Stayed",
        1: "Left"
    }
)

# High Risk Employee Flag
df["HighRiskEmployee"] = (
    (df["OverTime"] == "Yes") &
    (df["JobSatisfaction"] <= 2)
).astype(int)

# Verify New Columns
print("\nNew Columns Created")
print(df[
    [
        "AgeGroup",
        "IncomeGroup",
        "TenureGroup",
        "AttritionLabel",
        "HighRiskEmployee"
    ]
].head())

# Save Dataset
df.to_csv(
    "Data/Cleaned/HR_Analytics_Final.csv",
    index=False
)
