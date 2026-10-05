---
title: 0311 稀疏矩阵的乘法
date: 2026-09-10
---

## Solution

```python
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n = len(mat1), len(mat2[0])
        p = len(mat2)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(p):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply([[1,2],[3,4]], [[5,6],[7,8]]))
    # [[19,22],[43,50]]
```

## Solution 2

```python
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def f(mat: List[List[int]]) -> List[List[int]]:
            g = [[] for _ in range(len(mat))]
            for i, row in enumerate(mat):
                for j, x in enumerate(row):
                    if x:
                        g[i].append((j, x))
            return g

        g1 = f(mat1)
        g2 = f(mat2)
        m, n = len(mat1), len(mat2[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for k, x in g1[i]:
                for j, y in g2[k]:
                    ans[i][j] += x * y
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply([[1,0,0],[-1,0,3]],[[7,0,0],[0,0,0],[0,0,1]]))
    # [[7,0,0],[-7,0,3]]
```
