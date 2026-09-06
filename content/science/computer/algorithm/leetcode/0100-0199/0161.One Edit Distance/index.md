---
title: 0161 相隔为 1 的编辑距离
date: 2026-09-05
---

## Solution

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        m, n = len(s), len(t)
        if m - n > 1:
            return False
        for i, c in enumerate(t):
            if c != s[i]:
                return s[i + 1:] == t[i + 1:] if m == n else s[i + 1:] == t[i:]
        return m == n + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.isOneEditDistance("ab", "acb"))
    print(sol.isOneEditDistance("", ""))
    print(sol.isOneEditDistance("a", ""))
    print(sol.isOneEditDistance("cab", "ad"))
```
