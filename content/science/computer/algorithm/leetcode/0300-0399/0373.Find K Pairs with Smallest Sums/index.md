---
title: 0373 查找和最小的 K 对数字
date: 2026-09-18
---

## Solution

```python
from typing import List
import heapq

class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        q = [[u + nums2[0], i, 0] for i, u in enumerate(nums1[:k])]
        heapq.heapify(q)
        ans = []
        while q and k > 0:
            _, i, j = heapq.heappop(q)
            ans.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < len(nums2):
                heapq.heappush(q, [nums1[i] + nums2[j + 1], i, j + 1])
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.kSmallestPairs([1,7,11], [2,4,6], 3)) # [[1,2],[1,4],[1,6]]
    print(sol.kSmallestPairs([1,1,2], [1,2,3], 2)) # [[1,1],[1,1]]
```
