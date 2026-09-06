---
title: 0070 爬楼梯
date: 2026-08-16
weight: 70
summary: DP
---

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # 2
    print(sol.climbStairs(3))  # 3
    print(sol.climbStairs(4))  # 5
    print(sol.climbStairs(1))  # 1

```
