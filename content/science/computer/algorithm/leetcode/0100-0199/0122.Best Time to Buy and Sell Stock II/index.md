---
title: 0122 买卖股票的最佳时机 II
date: 2026-09-03
---

## Solution

```python
from typing import List
from itertools import pairwise

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, b - a) for a, b in pairwise(prices))


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4])) # 7
    print(sol.maxProfit([1,2,3,4,5]))    # 4
    print(sol.maxProfit([7,6,4,3,1]))    # 0
```

## Solution 2

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n)]
        f[0][0] = -prices[0]
        f[0][1] = 0
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] - prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 1][0] + prices[i])
        return f[n - 1][1]


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4])) # 7
    print(sol.maxProfit([1,2,3,4,5]))    # 4
    print(sol.maxProfit([7,6,4,3,1]))    # 0
```

## Solution 3

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [-prices[0], 0]
        for i in range(1, n):
            g = [0] * 2
            g[0] = max(f[0], f[1] - prices[i])
            g[1] = max(f[1], f[0] + prices[i])
            f = g
        return f[1]


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4])) # 7
    print(sol.maxProfit([1,2,3,4,5]))    # 4
    print(sol.maxProfit([7,6,4,3,1]))    # 0
```
