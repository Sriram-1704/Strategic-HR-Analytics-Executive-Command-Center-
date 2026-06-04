import pandas as pd

# Load Dataset
df = pd.read_csv("Data/Cleaned/HR_Analytics_Cleaned.csv")

print("Dataset Shape:", df.shape)

# Overall Attrition Rate
attrition_rate = round(
    (df["Attrition"].mean()) * 100,
    2
)
print("\nOverall Attrition Rate:")
print(attrition_rate)

# Correlation with Attrition
correlation = df.corr(numeric_only=True)["Attrition"]
top_correlations = (
    correlation
    .sort_values(ascending=False)
)
print("\nTop Correlations with Attrition:")
print(top_correlations)

# Average Monthly Income by Attrition
income_analysis = (
    df.groupby("Attrition")["MonthlyIncome"]
    .mean()
    .round(2)
)
print("\nAverage Monthly Income by Attrition:")
print(income_analysis)

# Attrition Rate by Business Travel
business_travel_attrition = (
    df.groupby("BusinessTravel")["Attrition"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)
print("\nAttrition Rate by Business Travel:")
print(business_travel_attrition)

# Attrition Rate by Job Level
joblevel_attrition = (
    df.groupby("JobLevel")["Attrition"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)
print("\nAttrition Rate by Job Level:")
print(joblevel_attrition)

# Average Years At Company
years_analysis = (
    df.groupby("Attrition")["YearsAtCompany"]
    .mean()
    .round(2)
)
print("\nAverage Years At Company:")
print(years_analysis)

# Attrition Rate by Department
department_attrition = (
    df.groupby("Department")["Attrition"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)
print("\nAttrition Rate by Department:")
print(department_attrition)

# Attrition Rate by Gender
gender_attrition = (
    df.groupby("Gender")["Attrition"]
    .mean()
    .mul(100)
    .round(2)
)
print("\nAttrition Rate by Gender:")
print(gender_attrition)

# Attrition Rate by OverTime
overtime_attrition = (
    df.groupby("OverTime")["Attrition"]
    .mean()
    .mul(100)
    .round(2)
)
print("\nAttrition Rate by OverTime:")
print(overtime_attrition)

# Create Summary Table

summary_table = pd.DataFrame({
    "Metric": [
        "Overall Attrition Rate",
        "Average Income (Stayed)",
        "Average Income (Left)",
        "Average Years At Company (Stayed)",
        "Average Years At Company (Left)"
    ],
    "Value": [
        attrition_rate,
        income_analysis.get(0),
        income_analysis.get(1),
        years_analysis.get(0),
        years_analysis.get(1)
    ]
})
print("\nSummary Table:")
print(summary_table)

# Export Summary Table
summary_table.to_excel(
    "Documentation/HR_Key_Insights.xlsx",
    index=False
)
print("\nKey Insights Exported Successfully")