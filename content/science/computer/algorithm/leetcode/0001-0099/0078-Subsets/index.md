---
title: 0078 子集
date: 2026-08-17
weight: 78
summary: 二叉回溯
---

## Solution

```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            if i == len(nums):
                ans.append(t[:])
                return
            dfs(i + 1)
            t.append(nums[i])
            dfs(i + 1)
            t.pop()

        ans = []
        t = []
        dfs(0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1,2,3]))

```
