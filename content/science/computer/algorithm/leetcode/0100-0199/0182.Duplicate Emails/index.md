---
title: 0182 查找重复出现的电子邮件
date: 2026-09-06
----

## Solution

```python
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    results = pd.DataFrame()
    results = person.loc[person.duplicated(subset=["email"]), ["email"]]
    return results.drop_duplicates()

if __name__ == "__main__":
    data = {"id":[1,2,3],"email":["a@b.com","c@d.com","a@b.com"]}
    df = pd.DataFrame(data)
    print(duplicate_emails(df))
```
