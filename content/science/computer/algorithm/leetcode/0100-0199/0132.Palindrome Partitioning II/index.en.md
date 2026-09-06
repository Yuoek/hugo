---
title: 0132.Palindrome Partitioning II
date: 2026-09-04
---

## Solution

```python
from typing import List

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # g[i][j]：s[i..j] 是否是回文
        g = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = s[i] == s[j] and g[i + 1][j - 1]
        
        # f[i]：s[0..i] 的最小分割次数
        f = list(range(n))
        for i in range(1, n):
            for j in range(i + 1):
                if g[j][i]:
                    if j == 0:
                        # s[0..i]本身就是回文，不需要切割
                        f[i] = 0
                    else:
                        f[i] = min(f[i], f[j - 1] + 1)
        return f[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCut("aab"))   # 1  "aa|b"
    print(sol.minCut("a"))     # 0
    print(sol.minCut("ab"))    # 1
    print(sol.minCut("abcba")) # 0
```
