---
title: 0119 杨辉三角 II
data: 2026-09-03
---

## Solution

```python
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        f = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                f[j] += f[j - 1]
        return f


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.getRow(3))   # [1,3,3,1]
    print(sol.getRow(0))   # [1]
    print(sol.getRow(4))   # [1,4,6,4,1]
```
