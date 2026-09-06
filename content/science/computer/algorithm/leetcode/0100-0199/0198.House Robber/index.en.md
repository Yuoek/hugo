---
title: 0198.House Robber
date: 2026-09-06
---

## Solution

```python
from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))
        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))
```

## Solution 2

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        f[1] = nums[0]
        for i in range(2, n + 1):
            f[i] = max(f[i - 1], f[i - 2] + nums[i - 1])
        return f[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))
```

## Solution 3

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        f = g = 0
        for x in nums:
            f, g = max(f, g), f + x
        return max(f, g)

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))
```
