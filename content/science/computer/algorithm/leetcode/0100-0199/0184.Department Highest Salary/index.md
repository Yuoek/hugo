---
title: 0184 部门工资最高的员工
date: 2026-09-06
---

## Solution

```python
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id')
    max_salaries = merged.groupby('departmentId')['salary'].transform('max')
    top_earners = merged[merged['salary'] == max_salaries]
    result = top_earners[['name_y', 'name_x', 'salary']].copy()
    result.columns = ['Department', 'Employee', 'Salary']
    return result

if __name__ == "__main__":
    emp = pd.DataFrame({
        "id":[1,2,3,4,5],
        "name":["Joe","Jim","Henry","Sam","Max"],
        "salary":[70000,90000,80000,60000,90000],
        "departmentId":[1,1,2,2,1]
    })
    dep = pd.DataFrame({
        "id":[1,2],
        "name":["IT","Sales"]
    })
    print(department_highest_salary(emp, dep))
```
