---
title: 0059 螺旋矩阵II
date: 2026-08-16
weight: 59
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        dirs = (0, 1, 0, -1, 0)
        i = j = k = 0
        for v in range(1, n * n + 1):
            ans[i][j] = v
            x, y = i + dirs[k], j + dirs[k + 1]
            if x < 0 or x >= n or y < 0 or y >= n or ans[x][y]:
                k = (k + 1) % 4
            i, j = i + dirs[k], j + dirs[k + 1]
        return ans

if __name__ == "__main__":
    sol = Solution()
    res = sol.generateMatrix(3)
    for row in res:
        print(row)

```
