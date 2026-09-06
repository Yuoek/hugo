---
title: 0048 图像旋转
date: 2026-08-15
weight: 48
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 上下翻转
        for i in range(n >> 1):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线转置
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    sol = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(mat)
    print(mat) # [[7,4,1],[8,5,2],[9,6,3]]
    mat2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(mat2)
    print(mat2)

```
