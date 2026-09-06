---
title: 0176 第二高的薪水
date: 2026-09-05
---

## Solution

```python
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee["salary"].drop_duplicates()
    second_highest = (
        unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None
    )
    if second_highest is None:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    result_df = pd.DataFrame({"SecondHighestSalary": [second_highest]})
    return result_df

if __name__ == "__main__":
    data1 = {"id":[1,2,3],"salary":[100,200,300]}
    df1 = pd.DataFrame(data1)
    print(second_highest_salary(df1))

    data2 = {"id":[1],"salary":[100]}
    df2 = pd.DataFrame(data2)
    print(second_highest_salary(df2))
```
