---
title: 0118.Pascal's Triangle
date: 2026-09-03
---

## Solution

```python
from typing import List
from itertools import pairwise

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        f = [[1]]
        for i in range(numRows - 1):
            g = [1] + [a + b for a, b in pairwise(f[-1])] + [1]
            f.append(g)
        return f


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))
    # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(sol.generate(1))
    # [[1]]
```
