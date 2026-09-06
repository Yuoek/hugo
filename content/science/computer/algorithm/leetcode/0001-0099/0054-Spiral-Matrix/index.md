---
title: 0054 螺旋矩阵
date: 2026-08-16
weight: 54
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = (0, 1, 0, -1, 0)
        vis = [[False] * n for _ in range(m)]
        i = j = k = 0
        ans = []
        for _ in range(m * n):
            ans.append(matrix[i][j])
            vis[i][j] = True
            x, y = i + dirs[k], j + dirs[k + 1]
            if x < 0 or x >= m or y < 0 or y >= n or vis[x][y]:
                k = (k + 1) % 4
            i += dirs[k]
            j += dirs[k + 1]
        return ans

if __name__ == "__main__":
    sol = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.spiralOrder(mat))

```
