---
title: 0034 在排序数组中查找元素的第一个和最后一个位置
date: 2026-08-14
weight: 34
summary: 二分
---

## Solution

```python
from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_left(nums, target + 1)
        return [-1, -1] if l == r else [l, r - 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10],8)) # [3,4]
    print(sol.searchRange([5,7,7,8,8,10],6)) # [-1,-1]
    print(sol.searchRange([],0))             # [-1,-1]
    print(sol.searchRange([2,2],2))          # [0,1]

```
