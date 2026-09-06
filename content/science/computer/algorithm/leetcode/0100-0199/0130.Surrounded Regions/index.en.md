---
title: 0130.Surrounded Regions
date: 2026-09-04
---

## Solution

```python
from typing import List
from itertools import pairwise

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i: int, j: int):
            if not (0 <= i < m and 0 <= j < n and board[i][j] == "O"):
                return
            board[i][j] = "."
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                dfs(i + a, j + b)

        m, n = len(board), len(board[0])
        # 遍历左右两列边界
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        # 遍历上下两行边界
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        # 复原 & 替换
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    sol.solve(board)
    for row in board:
        print(row)
"""
输出：
['X', 'X', 'X', 'X']
['X', 'X', 'X', 'X']
['X', 'X', 'X', 'X']
['X', 'O', 'X', 'X']
"""
```

## Solution 2

```python
from typing import List
from itertools import pairwise

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        m, n = len(board), len(board[0])
        # 虚拟节点编号：m*n，代表边界连通集合
        p = list(range(m * n + 1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    # 边界O：合并到虚拟根 m*n
                    if i in (0, m - 1) or j in (0, n - 1):
                        p[find(i * n + j)] = find(m * n)
                    else:
                        # 上下左右四个方向
                        for a, b in pairwise((-1, 0, 1, 0, -1)):
                            x, y = i + a, j + b
                            if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                                p[find(x * n + y)] = find(i * n + j)
        # 不跟虚拟根连通的O → 改为X
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and find(i * n + j) != find(m * n):
                    board[i][j] = "X"


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    sol.solve(board)
    for row in board:
        print(row)
"""
输出：
['X', 'X', 'X', 'X']
['X', 'X', 'X', 'X']
['X', 'X', 'X', 'X']
['X', 'O', 'X', 'X']
"""
```
