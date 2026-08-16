---
title: 0064 最小路径
date: 2026-08-16
weight: 64
summary: DP
---

## Solution

```python
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[0] * n for _ in range(m)]
        f[0][0] = grid[0][0]
        for i in range(1, m):
            f[i][0] = f[i - 1][0] + grid[i][0]
        for j in range(1, n):
            f[0][j] = f[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]
        return f[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])) # 7
    print(sol.minPathSum([[1,2,3],[4,5,6]]))         # 12

```
