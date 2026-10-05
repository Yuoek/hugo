---
title: 0330 按要求补齐数组
date: 2026-09-17
---

## Solution

```python
from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        x = 1
        ans = i = 0
        while x <= n:
            if i < len(nums) and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                ans += 1
                x <<= 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.minPatches([1,3], 6))    # 1
    print(sol.minPatches([1,5,10], 20)) # 2
    print(sol.minPatches([1,2,2], 5))  # 0

```
