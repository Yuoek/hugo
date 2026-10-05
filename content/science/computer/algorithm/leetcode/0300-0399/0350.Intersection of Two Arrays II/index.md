---
title: 0350 两个数组的交集 II
date: 2026-09-18
---

## Solution

```python
from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x]:
                ans.append(x)
                cnt[x] -= 1
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1,2,2,1], [2,2]))        # [2, 2]
    print(sol.intersect([4,9,5], [9,4,9,8,4]))    # [4,9]
    print(sol.intersect([1,2,3], []))             # []
```
