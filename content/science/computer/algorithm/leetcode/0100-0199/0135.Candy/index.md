---
title: 0135 分发糖果
date: 2026-09-04
---

## Solution

```python
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        return sum(max(a, b) for a, b in zip(left, right))


if __name__ == "__main__":
    sol = Solution()
    print(sol.candy([1,0,2]))    # 5
    print(sol.candy([1,2,2]))    # 4
    print(sol.candy([1,3,2,1]))  # 7
```
