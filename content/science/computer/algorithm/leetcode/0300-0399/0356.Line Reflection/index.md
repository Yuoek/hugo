---
title: 0356 直线镜像
date: 2026-09-18
---

## Solution

```python
from typing import List
from math import inf

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        min_x, max_x = inf, -inf
        point_set = set()
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            point_set.add((x, y))
        s = min_x + max_x
        return all((s - x, y) in point_set for x, y in points)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.isReflected([[1,1],[-1,1]])) # True 对称轴 x=0
    print(sol.isReflected([[1,1],[-1,-1]])) # False
    print(sol.isReflected([[0,0],[1,0]])) # True 对称轴 x=0.5
```
