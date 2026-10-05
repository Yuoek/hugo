---
title: 0361 轰炸敌人
date: 2026-09-18
---

## Solution

```python
from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        g = [[0] * n for _ in range(m)]
        for i in range(m):
            t = 0
            for j in range(n):
                if grid[i][j] == 'W':
                    t = 0
                elif grid[i][j] == 'E':
                    t += 1
                g[i][j] += t
            t = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 'W':
                    t = 0
                elif grid[i][j] == 'E':
                    t += 1
                g[i][j] += t
        for j in range(n):
            t = 0
            for i in range(m):
                if grid[i][j] == 'W':
                    t = 0
                elif grid[i][j] == 'E':
                    t += 1
                g[i][j] += t
            t = 0
            for i in range(m - 1, -1, -1):
                if grid[i][j] == 'W':
                    t = 0
                elif grid[i][j] == 'E':
                    t += 1
                g[i][j] += t
        return max(
            [g[i][j] for i in range(m) for j in range(n) if grid[i][j] == '0'],
            default=0,
        )

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    grid = [
        ["0","E","0","0"],
        ["E","0","W","E"],
        ["0","E","0","0"]
    ]
    print(sol.maxKilledEnemies(grid)) # 3
    grid2 = [["W","W","W"],["W","W","W"],["W","W","W"]]
    print(sol.maxKilledEnemies(grid2)) # 0
```
