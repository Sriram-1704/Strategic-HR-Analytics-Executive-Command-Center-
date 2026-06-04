import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Data/Cleaned/HR_Analytics_Cleaned.csv")
print("Dataset Shape:", df.shape)

sns.set_style("whitegrid")

# 1. Attrition Count Plot
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="Attrition"
)
plt.title("Employee Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.savefig("Visualizations/EDA_Charts/01_Attrition_Count.png")
plt.show()

# 2. Attrition Rate by Department
department_attrition = (
    df.groupby("Department")["Attrition"]
    .mean()
    .sort_values(ascending=False)
)
plt.figure(figsize=(8, 5))
department_attrition.plot(
    kind="bar"
)
plt.title("Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate")
plt.tight_layout()
plt.savefig("Visualizations/EDA_Charts/02_Attrition_By_Department.png")
plt.show()

# 3. Monthly Income vs Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Attrition",
    y="MonthlyIncome"
)
plt.title("Monthly Income vs Attrition")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income")
plt.tight_layout()
plt.savefig("Visualizations/EDA_Charts/03_MonthlyIncome_vs_Attrition.png")
plt.show()

# 4. Correlation Heatmap
numeric_df = df.select_dtypes(
    include=["int64", "float64"]
)
plt.figure(figsize=(15,10))
sns.heatmap(
    numeric_df.corr(),
    annot=False,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("Visualizations/EDA_Charts/04_Correlation_Heatmap.png")
plt.show()

# 5. Age Distribution by Attrition
plt.figure(figsize=(8,5))
sns.histplot(
    data=df,
    x="Age",
    hue="Attrition",
    kde=True
)
plt.title("Age Distribution by Attrition")
plt.xlabel("Age")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.savefig("Visualizations/EDA_Charts/05_Age_Distribution.png")
plt.show()

# 6. OverTime vs Attrition
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="OverTime",
    hue="Attrition"
)
plt.title("OverTime vs Attrition")
plt.xlabel("OverTime")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.savefig("Visualizations/EDA_Charts/06_OverTime_vs_Attrition.png")
plt.show()


# 7. Job Satisfaction vs Attrition
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="JobSatisfaction",
    hue="Attrition"
)
plt.title("Job Satisfaction vs Attrition")
plt.xlabel("Job Satisfaction")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.savefig("Visualizations/EDA_Charts/07_JobSatisfaction_vs_Attrition.png")
plt.show()


# 8. Work Life Balance vs Attrition
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="WorkLifeBalance",
    hue="Attrition"
)
plt.title("Work Life Balance vs Attrition")
plt.xlabel("Work Life Balance")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.savefig("Visualizations/EDA_Charts/08_WorkLifeBalance_vs_Attrition.png")
plt.show()

# EDA Completed
print("EDA Completed Successfully")
