---
title: 0312.Burst Balloons
date: 2026-09-10
---

## Solution

```python
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] + nums + [1]
        f = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j])
        return f[0][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxCoins([3,1,5,8])) # 167
    print(sol.maxCoins([1,5])) #10
```
