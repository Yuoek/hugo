---
title: 0062 不同路径
date: 2026-08-16
weight: 62
summary: DP
---

## Solution

```python
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * n for _ in range(m)]
        f[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i:
                    f[i][j] += f[i - 1][j]
                if j:
                    f[i][j] += f[i][j - 1]
        return f[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3,7))  # 28
    print(sol.uniquePaths(3,2))  # 3
    print(sol.uniquePaths(1,1))  # 1

```
