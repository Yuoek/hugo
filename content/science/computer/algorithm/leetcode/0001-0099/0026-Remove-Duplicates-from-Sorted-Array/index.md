---
title: 0026 删除有序数组中的重复项
date: 2026-08-14
weight: 26
summary: 快慢指针
---

## Solution

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k

if __name__ == "__main__":
    sol = Solution()
    arr1 = [1,1,2]
    print(sol.removeDuplicates(arr1))
    print(arr1)

    arr2 = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(arr2))
    print(arr2)

```
