---
titel: 0196 删除重复邮件
date: 2026-09-06
---

## Solution

```python
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", ascending=True, inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)

if __name__ == "__main__":
    data = {"id":[2,1,3],"email":["a@b.com","a@b.com","c@b.com"]}
    df = pd.DataFrame(data)
    delete_duplicate_emails(df)
    print(df)
```
