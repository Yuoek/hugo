---
title: 0188 买卖股票的最佳时期 IV
date: 2026-09-06
---

## Solution

```python
from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, hold: int) -> int:
            if i >= len(prices):
                return 0
            ans = dfs(i + 1, j, hold)
            if hold:
                ans = max(ans, prices[i] + dfs(i + 1, j, 0))
            elif j > 0:
                ans = max(ans, -prices[i] + dfs(i + 1, j - 1, 1))
            return ans
        return dfs(0, k, 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(2,[2,4,1]))
    print(sol.maxProfit(2,[3,2,6,5,0,3]))
```

## Solution 2

```python
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        f = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        for j in range(1, k + 1):
            f[0][j][1] = -prices[0]
        for i, x in enumerate(prices[1:], 1):
            for j in range(1, k + 1):
                f[i][j][0] = max(f[i - 1][j][1] + x, f[i - 1][j][0])
                f[i][j][1] = max(f[i - 1][j - 1][0] - x, f[i - 1][j][1])
        return f[n - 1][k][0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(2, [2,4,1]))
    print(sol.maxProfit(2, [3,2,6,5,0,3]))
```

## Solution 3

```python
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        f = [[0] * 2 for _ in range(k + 1)]
        for j in range(1, k + 1):
            f[j][1] = -prices[0]
        for x in prices[1:]:
            for j in range(k, 0, -1):
                f[j][0] = max(f[j][1] + x, f[j][0])
                f[j][1] = max(f[j - 1][0] - x, f[j][1])
        return f[k][0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(2, [2,4,1]))
    print(sol.maxProfit(2, [3,2,6,5,0,3]))
```
