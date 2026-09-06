---
title: 0096 不同的二叉搜索树
date: 2026-08-17
weight: 96
summary: 卡特兰树DP
---

## Solution

```python
from typing import List

class Solution:
    def numTrees(self, n: int) -> int:
        f = [1] + [0] * n
        for i in range(1, n + 1):
            for j in range(i):
                f[i] += f[j] * f[i - j - 1]
        return f[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numTrees(3)) # 5
    print(sol.numTrees(4)) # 14

```
