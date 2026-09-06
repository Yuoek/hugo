---
title: 0081 搜索旋转排序数组 II
date: 2026-08-17
weight: 81
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:
                r -= 1
        return nums[l] == target

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([2,5,6,0,0,1,2], 0))   # True
    print(sol.search([2,2,2,0,2,2], 0))     # True
    print(sol.search([1,0,1,1,1], 0))       # True

```

