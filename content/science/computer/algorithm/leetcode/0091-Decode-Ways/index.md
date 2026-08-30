---
title: 0091 解码方法
date: 2026-08-17
weight: 91
summary: 一维DP
---

## Solution

```python
from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i, c in enumerate(s, 1):
            if c != "0":
                f[i] = f[i - 1]
            if i > 1 and s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
                f[i] += f[i - 2]
        return f[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))   # 2
    print(sol.numDecodings("226"))  # 3
    print(sol.numDecodings("06"))   # 0

```
