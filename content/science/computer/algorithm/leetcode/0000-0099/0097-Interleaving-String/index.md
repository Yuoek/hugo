---
title: 0097 交错字符串
date: 2026-08-17
weight: 97
summary: 记忆化DP
---

## Solution

```python
from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> bool:
            if i >= m and j >= n:
                return True
            k = i + j
            if i < m and s1[i] == s3[k] and dfs(i + 1, j):
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j + 1):
                return True
            return False

        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        return dfs(0, 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")) # True
    print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc")) # False

```
