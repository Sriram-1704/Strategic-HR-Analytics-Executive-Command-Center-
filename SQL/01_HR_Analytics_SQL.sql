-- Total Employees
SELECT
    COUNT(*) AS Total_Employees
FROM HR_Analytics_Final;

-- Overall Attrition Rate
SELECT
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate_Percentage
FROM HR_Analytics_Final;

-- Attrition Rate by Department
SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(Attrition) AS Employees_Left,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY Department
ORDER BY Attrition_Rate DESC;

-- Attrition by Gender
SELECT
    Gender,
    COUNT(*) AS Total_Employees,
    SUM(Attrition) AS Employees_Left,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY Gender
ORDER BY Attrition_Rate DESC;

-- Attrition by Marital Status
SELECT
    MaritalStatus,
    COUNT(*) AS Total_Employees,
    SUM(Attrition) AS Employees_Left,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY MaritalStatus
ORDER BY Attrition_Rate DESC;

-- Overtime vs Attrition
SELECT
    OverTime,
    COUNT(*) AS Total_Employees,
    SUM(Attrition) AS Employees_Left,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY OverTime
ORDER BY Attrition_Rate DESC;

-- Top 5 High Attrition Job Roles
SELECT
    JobRole,
    COUNT(*) AS Employees,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY JobRole
ORDER BY Attrition_Rate DESC
LIMIT 5;

-- Average Monthly Income by Job Role
SELECT
    JobRole,
    ROUND(AVG(MonthlyIncome), 2) AS Avg_Monthly_Income
FROM HR_Analytics_Final
GROUP BY JobRole
ORDER BY Avg_Monthly_Income DESC;

--  Average Tenure, Employees Who Left vs Stayed
SELECT
    AttritionLabel,
    ROUND(AVG(YearsAtCompany), 2) AS Avg_Years_At_Company
FROM HR_Analytics_Final
GROUP BY AttritionLabel;

-- Performance Rating vs Salary
SELECT
    PerformanceRating,
    ROUND(AVG(MonthlyIncome), 2) AS Avg_Monthly_Income
FROM HR_Analytics_Final
GROUP BY PerformanceRating
ORDER BY PerformanceRating;

--  Attrition by Job Level
SELECT
    JobLevel,
    COUNT(*) AS Employees,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY JobLevel
ORDER BY Attrition_Rate DESC;

-- Attrition by Age Group
SELECT
    AgeGroup,
    COUNT(*) AS Employees,
    SUM(Attrition) AS Employees_Left,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY AgeGroup
ORDER BY Attrition_Rate DESC;

-- Attrition by Business Travel
SELECT
    BusinessTravel,
    COUNT(*) AS Employees,
    SUM(Attrition) AS Employees_Left,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY BusinessTravel
ORDER BY Attrition_Rate DESC;

-- Attrition by Education Field
SELECT
    EducationField,
    COUNT(*) AS Employees,
    SUM(Attrition) AS Employees_Left,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY EducationField
ORDER BY Attrition_Rate DESC;

-- High Risk Employees
SELECT
    COUNT(*) AS High_Risk_Employees
FROM HR_Analytics_Final
WHERE HighRiskEmployee = 1;

-- Department-wise Average Salary
SELECT
    Department,
    ROUND(AVG(MonthlyIncome), 2) AS Avg_Monthly_Income
FROM HR_Analytics_Final
GROUP BY Department
ORDER BY Avg_Monthly_Income DESC;

-- Work Life Balance vs Attrition
SELECT
    WorkLifeBalance,
    COUNT(*) AS Employees,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY WorkLifeBalance
ORDER BY Attrition_Rate DESC;

-- Job Satisfaction vs Attrition
SELECT
    JobSatisfaction,
    COUNT(*) AS Employees,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY JobSatisfaction
ORDER BY Attrition_Rate DESC;

-- Environment Satisfaction vs Attrition
SELECT
    EnvironmentSatisfaction,
    COUNT(*) AS Employees,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY EnvironmentSatisfaction
ORDER BY Attrition_Rate DESC;

-- Department × Job Level Attrition Matrix
SELECT
    Department,
    JobLevel,
    COUNT(*) AS Employees,
    ROUND(AVG(Attrition) * 100, 2) AS Attrition_Rate
FROM HR_Analytics_Final
GROUP BY Department, JobLevel
ORDER BY Department, JobLevel;
