---
title: 0180 连续出现最大的数
date: 2026-09-06
---

## Solution

```python
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    all_the_same = lambda lst: lst.nunique() == 1
    logs["is_consecutive"] = (
        logs["num"].rolling(window=3, center=True, min_periods=3).apply(all_the_same)
    )
    return (
        logs.query("is_consecutive == 1.0")[["num"]]
        .drop_duplicates()
        .rename(columns={"num": "ConsecutiveNums"})
    )

if __name__ == "__main__":
    data = {"id":[1,2,3,4,5,6,7],"num":[1,1,1,2,1,2,2]}
    df = pd.DataFrame(data)
    print(consecutive_numbers(df))
```
