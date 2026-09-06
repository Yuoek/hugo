---
title: 0123 买卖股票 III
date: 2026-09-03
---

## Solution

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # f1:第i天第一次持有 f2:第一次卖出 f3:第二次持有 f4:第二次卖出
        f1, f2, f3, f4 = -prices[0], 0, -prices[0], 0
        for price in prices[1:]:
            f1 = max(f1, -price)
            f2 = max(f2, f1 + price)
            f3 = max(f3, f2 - price)
            f4 = max(f4, f3 + price)
        return f4


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([3,3,5,0,0,3,1,4])) #6
    print(sol.maxProfit([1,2,3,4,5]))       #4
    print(sol.maxProfit([7,6,4,3,1]))       #0
```
