---
title: 0121 买卖股票的最佳时机
date: 2026-09-03
---

## Solution

```python
from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, mi = 0, math.inf
        for v in prices:
            ans = max(ans, v - mi)
            mi = min(mi, v)
        return ans


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4])) # 5
    print(sol.maxProfit([7,6,4,3,1]))   # 0
```
