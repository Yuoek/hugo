---
title: 0153.Find Minimum in Rotated Sorted Array
date: 2026-09-05
---

## Solution

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3,4,5,1,2]))
    print(sol.findMin([4,5,6,7,0,1,2]))
    print(sol.findMin([11,13,15,17]))
```
