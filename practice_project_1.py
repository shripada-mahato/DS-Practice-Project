import pandas as pd
data = pd.read_csv("employee_data_ds_practice.csv")
print("Original Dataset:- \n",data.to_string())
print("First five column:- \n",data.head(5))
print("Find the number of rows and columns:- \n",data.shape)
print("Display all column names. \n", data.columns)
print("Check the data types. \n", data.dtypes)
print("Check for missing values. \n",data.isnull())
name_department_salary = data[['Name','Department','Salary']]
print("Display only Name, Department, and Salary. \n",name_department_salary)
emp_slry_45k = data[data['Salary']>45000]
print("Find employees whose salary is greater than 45000. \n", emp_slry_45k)
it_dept = data[data['Department']=='IT']
print("It Dept Emp:- \n", it_dept)
slry_HL = data.sort_values('Salary',ascending=True)
print("Highest to lowest Salary:- \n", slry_HL)