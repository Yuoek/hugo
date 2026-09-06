---
title: 0115 不同的子序列
date: 2026-09-03
---

## Solution

```python
from typing import List

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        # t为空串，s任意，方案数为1
        for i in range(m + 1):
            f[i][0] = 1
        for i, a in enumerate(s, 1):
            for j, b in enumerate(t, 1):
                f[i][j] = f[i - 1][j]
                if a == b:
                    f[i][j] += f[i - 1][j - 1]
        return f[m][n]


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDistinct("rabbbit", "rabbit")) # 3
    print(sol.numDistinct("babgbag", "bag"))    # 5
    print(sol.numDistinct("", ""))              # 1
    print(sol.numDistinct("a", ""))             # 1
    print(sol.numDistinct("", "a"))             # 0
```

## Solution 2

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        f = [1] + [0] * n
        for a in s:
            for j in range(n, 0, -1):
                if a == t[j - 1]:
                    f[j] += f[j - 1]
        return f[n]


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDistinct("rabbbit", "rabbit"))  # 3
    print(sol.numDistinct("babgbag", "bag"))     # 5
    print(sol.numDistinct("", ""))               # 1
    print(sol.numDistinct("a", ""))              # 1
    print(sol.numDistinct("", "a"))              # 0
```
