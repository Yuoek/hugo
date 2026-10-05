---
title: 0349 两个数组的交集
date: 2026-09-17
---

## Solution

```python
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([1,2,2,1], [2,2])) # [2]
    print(sol.intersection([4,9,5], [9,4,9,8,4,5])) # [9,4,5]
```
