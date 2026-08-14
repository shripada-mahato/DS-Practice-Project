
# 📊 Employee Data Analysis — Pandas, NumPy & Matplotlib

A practical Data Science project focused on analyzing employee data using **Python, Pandas, NumPy, and Matplotlib**.

The purpose of this project is not just to learn individual library functions, but to understand how different Data Science libraries work together in a real-world data analysis workflow.

---

## 🎯 Project Objective

The project analyzes an employee dataset containing information such as:

- Employee ID
- Name
- Department
- Age
- Salary
- Experience
- Performance Score
- Projects Completed

The analysis covers data inspection, filtering, numerical calculations, grouping, and visualization.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** — Data loading, filtering, grouping and manipulation
- **NumPy** — Numerical calculations and array operations
- **Matplotlib** — Data visualization
- **Jupyter Notebook / VS Code** — Development environment
- **Git & GitHub** — Version control and project management

---

## 📂 Dataset

The project uses an employee dataset in CSV format.

### Main columns

| Column | Description |
|---|---|
| `Employee_ID` | Unique employee identifier |
| `Name` | Employee name |
| `Department` | Employee's department |
| `Age` | Employee age |
| `Salary` | Employee salary |
| `Experience_Years` | Years of professional experience |
| `Performance_Score` | Employee performance score |
| `Projects_Completed` | Number of completed projects |

---

## 🔎 Analysis Performed

### 1. Data Inspection

Using Pandas:

- Loaded the CSV dataset
- Displayed the complete dataset
- Viewed the first five rows
- Checked dataset dimensions
- Examined column names
- Checked data types
- Checked for missing values

### 2. Data Filtering

Performed filtering operations such as:

- Selecting specific columns
- Finding employees with salary greater than ₹45,000
- Filtering employees from the IT department
- Sorting employees by salary

### 3. Numerical Analysis with NumPy

Used NumPy to analyze salary data:

- Converted salary data into a NumPy array
- Calculated average salary
- Found maximum salary
- Found minimum salary
- Calculated the difference between maximum and minimum salary
- Performed salary calculations

### 4. Grouped Analysis

Used Pandas `groupby()` to calculate:

- Department-wise average salary

### 5. Data Visualization

Created visualizations using Matplotlib:

- 📊 Department-wise average salary — Bar Chart
- 🔵 Experience vs Salary — Scatter Plot
- 📈 Salary distribution — Histogram
- 🔲 Subplot visualization — In progress

---

## 🔄 Data Science Workflow

The main learning approach used in this project is:

```text
Raw Dataset
     ↓
Pandas
Load & Inspect Data
     ↓
Pandas
Filter & Group Data
     ↓
NumPy
Numerical Analysis
     ↓
Pandas
Organize Results
     ↓
Matplotlib
Visualize Data
     ↓
Interpret Results