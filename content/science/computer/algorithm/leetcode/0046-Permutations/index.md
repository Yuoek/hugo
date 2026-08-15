---
title: 0046 全排列
date: 2026-08-15
weight: 46
summary: DFS
---

## Solution

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            if i >= n:
                ans.append(t[:])
                return
            for j, x in enumerate(nums):
                if not vis[j]:
                    vis[j] = True
                    t[i] = x
                    dfs(i + 1)
                    vis[j] = False

        n = len(nums)
        vis = [False] * n
        t = [0] * n
        ans = []
        dfs(0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3]))
    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(sol.permute([0,1]))
    print(sol.permute([1]))
```
