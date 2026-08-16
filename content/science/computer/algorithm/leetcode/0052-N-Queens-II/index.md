---
title: 0052.N-Queens II
date: 2026-08-16
weight: 52
summary: DFS 回溯
---

## Solution

```python
from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(i: int):
            if i == n:
                nonlocal ans
                ans += 1
                return
            for j in range(n):
                a, b = i + j, i - j + n
                if cols[j] or dg[a] or udg[b]:
                    continue
                cols[j] = dg[a] = udg[b] = True
                dfs(i + 1)
                cols[j] = dg[a] = udg[b] = False

        cols = [False] * 20
        dg = [False] * 40
        udg = [False] * 40
        ans = 0
        dfs(0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNQueens(4))
    print(sol.totalNQueens(8))

```
