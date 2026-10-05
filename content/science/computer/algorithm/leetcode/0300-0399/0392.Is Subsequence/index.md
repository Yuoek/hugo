---
title: 0392 判断子序列
date: 2026-09-18
---

## Solution

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc")) # True
    print(sol.isSubsequence("axc", "ahbgdc")) # False
    print(sol.isSubsequence("", "abc")) # True
```
