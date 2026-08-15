---
title: 0027 移除元素
date: 2026-08-14
weight: 27
summary: 双指针
---

## Solution

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k

if __name__ == "__main__":
    sol = Solution()
    arr1 = [3,2,2,3]
    print(sol.removeElement(arr1,3))
    print(arr1)

    arr2 = [0,1,2,2,3,0,4,2]
    print(sol.removeElement(arr2,2))
    print(arr2)

```
