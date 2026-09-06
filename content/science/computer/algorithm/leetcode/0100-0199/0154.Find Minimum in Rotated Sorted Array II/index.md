---
title: 0154 寻找旋转排序数组中最小的值 II
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
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] == nums[r]:
                r -= 1
            else:
                r = mid
        return nums[l]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([2,2,2,0,1]))
    print(sol.findMin([3,4,5,1,2]))
    print(sol.findMin([1,3,5]))
```
