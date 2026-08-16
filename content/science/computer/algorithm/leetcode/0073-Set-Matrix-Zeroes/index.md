---
title: 0073 矩阵置零
date: 2026-08-16
weight: 73
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row = [False] * m
        col = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

if __name__ == "__main__":
    sol = Solution()
    mat1 = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(mat1)
    print(mat1) # [[1,0,1],[0,0,0],[1,0,1]]

    mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(mat2)
    print(mat2) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```
