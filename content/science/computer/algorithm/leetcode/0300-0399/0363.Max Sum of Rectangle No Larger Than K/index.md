---
title: 0363 矩形区域不超过 K 的最大数值和
date: 2026-09-18
---

## Solution

```python
from typing import List
from math import inf
from sortedcontainers import SortedSet

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -inf
        for i in range(m):
            nums = [0] * n
            for j in range(i, m):
                for h in range(n):
                    nums[h] += matrix[j][h]
                s = 0
                ts = SortedSet([0])
                for x in nums:
                    s += x
                    p = ts.bisect_left(s - k)
                    if p != len(ts):
                        ans = max(ans, s - ts[p])
                    ts.add(s)
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2)) # 2
    print(sol.maxSumSubmatrix([[2,-1,2]], 3)) # 3
```
