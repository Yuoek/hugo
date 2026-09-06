---
title: 0181 超过经理收入的员工
date: 2026-09-06
---

## Solution

```python
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        employee, left_on="managerId", right_on="id", suffixes=("", "_manager")
    )
    result = merged[merged["salary"] > merged["salary_manager"]][["name"]]
    result.columns = ["Employee"]
    return result

if __name__ == "__main__":
    data = {
        "id":[1,2,3,4,5],
        "name":["Joe","Henry","Sam","Max","Janet"],
        "salary":[70000,80000,60000,90000,70000],
        "managerId":[3,4,None,None,3]
    }
    df = pd.DataFrame(data)
    print(find_employees(df))
```
