---
title: 0035 搜索插入位置
date: 2026-08-14
weight: 35
summary: 二分
---

## Solution

```python
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6],5))  # 2
    print(sol.searchInsert([1,3,5,6],2))  # 1
    print(sol.searchInsert([1,3,5,6],7))  # 4
    print(sol.searchInsert([1,3,5,6],0))  # 0

```
