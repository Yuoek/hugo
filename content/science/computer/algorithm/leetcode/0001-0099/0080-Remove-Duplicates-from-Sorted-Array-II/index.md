---
title: 0080 删除有序数组中重复项 II
date: 2026-08-17
weight: 80
summary: 快慢指针
---

## Solution

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k

if __name__ == "__main__":
    sol = Solution()
    arr = [1,1,1,2,2,3]
    print(sol.removeDuplicates(arr))
    print(arr)

```
