---
title: 0044 通配符匹配
date: 2026-08-15
weight: 44
summary: 记忆化DFS
---

## Solution

```python
from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> bool:
            if i >= len(s):
                return j >= len(p) or (p[j] == "*" and dfs(i, j + 1))
            if j >= len(p):
                return False
            if p[j] == "*":
                return dfs(i + 1, j) or dfs(i + 1, j + 1) or dfs(i, j + 1)
            return (p[j] == "?" or s[i] == p[j]) and dfs(i + 1, j + 1)

        return dfs(0, 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))      # False
    print(sol.isMatch("aa", "*"))      # True
    print(sol.isMatch("cb", "?a"))     # False
    print(sol.isMatch("adceb", "*a*b"))# True

```


记忆缓存：@lru_cache(maxsize=None)

情况	返回
s 空，p 也空	True
s 空，p 剩下*	True（吃掉星号）
s 空，p 剩下普通字符	False
p 空，s 还有字符	False
遇到*	匹配字符(保留*) or 匹配空(消耗*)，一条通就 True
普通字符 ?	当前位置匹配 并且 后缀也匹配，才 True
