---
title: 0149.Max Points on a Line
date: 2026-09-05
---

## Solution

```python
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 1
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cnt = 2
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    a = (y2 - y1) * (x3 - x1)
                    b = (y3 - y1) * (x2 - x1)
                    cnt += a == b
                ans = max(ans, cnt)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPoints([[1,1],[2,2],[3,3]]))
    print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
```

## Solution

```python
from typing import List
from collections import Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        n = len(points)
        ans = 1
        for i in range(n):
            x1, y1 = points[i]
            cnt = Counter()
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dx, dy)
                k = (dx // g, dy // g)
                cnt[k] += 1
                ans = max(ans, cnt[k] + 1)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPoints([[1,1],[2,2],[3,3]]))
    print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
```
