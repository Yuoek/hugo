---
title: 0077 组合
date: 2026-08-17
weight: 77
summary: DFS 回溯
---

## Solution

```python
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i: int):
            if len(t) == k:
                ans.append(t[:])
                return
            if i > n:
                return
            t.append(i)
            dfs(i + 1)
            t.pop()
            dfs(i + 1)

        ans = []
        t = []
        dfs(1)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(4,2))
    # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

```
