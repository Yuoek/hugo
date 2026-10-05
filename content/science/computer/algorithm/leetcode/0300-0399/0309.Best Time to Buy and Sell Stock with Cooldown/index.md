---
title: 0309 买卖股票的最佳时机含冷冻期
date: 2026-09-09
---

## Solution

```python
from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= len(prices):
                return 0
            ans = dfs(i + 1, j)
            if j:
                ans = max(ans, prices[i] + dfs(i + 2, 0))
            else:
                ans = max(ans, -prices[i] + dfs(i + 1, 1))
            return ans

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1,2,3,0,2])) #3
    print(sol.maxProfit([1])) #0
```

## Solution 2

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        f = [[0] * 2 for _ in range(n)]
        f[0][1] = -prices[0]
        f[1][0] = max(0, f[0][1] + prices[1])
        f[1][1] = max(-prices[0], -prices[1])
        for i in range(2, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 2][0] - prices[i])
        return f[n - 1][0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1,2,3,0,2])) # 3
    print(sol.maxProfit([1])) # 0
```

## Solution

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        f, f0, f1 = 0, 0, -prices[0]
        for x in prices[1:]:
            f, f0, f1 = f0, max(f0, f1 + x), max(f1, f - x)
        return f0


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1,2,3,0,2])) #3
    print(sol.maxProfit([1])) #0
```
