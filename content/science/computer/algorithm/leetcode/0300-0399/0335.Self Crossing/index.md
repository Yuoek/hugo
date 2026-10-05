---
title: 0335 路径交叉
date: 2026-09-17
---

## Solution

```python
from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        d = distance
        for i in range(3, len(d)):
            # Case1: 第i圈直接跨到i-3边
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True
            # Case2: i >=4，和i-4边重合相交
            if i >= 4 and d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
                return True
            # Case3: i >=5，跨到i-5的边
            if (
                i >= 5
                and d[i - 2] >= d[i - 4]
                and d[i - 1] <= d[i - 3]
                and d[i] >= d[i - 2] - d[i - 4]
                and d[i - 1] + d[i - 5] >= d[i - 3]
            ):
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isSelfCrossing([2,1,1,2]))    # True
    print(sol.isSelfCrossing([1,2,3,4]))    # False
    print(sol.isSelfCrossing([1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1])) # True
```
