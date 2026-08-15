---
title: 0039 组合总和
date: 2026-08-14
weight: 39
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, s: int):
            if s == 0:
                ans.append(t[:])
                return
            if s < candidates[i]:
                return
            for j in range(i, len(candidates)):
                t.append(candidates[j])
                dfs(j, s - candidates[j])
                t.pop()

        candidates.sort()
        t = []
        ans = []
        dfs(0, target)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,3,6,7],7))   # [[2,2,3],[7]]
    print(sol.combinationSum([2,3,5],8))    # [[2,2,2,2],[2,3,3],[3,5]]
    print(sol.combinationSum([2],1))        # []

```
