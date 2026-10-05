---
title: 0389.Find the Difference
date: 2026-09-18
---

## Solution

```python
from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1
            if cnt[c] < 0:
                return c

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde")) # 'e'
    print(sol.findTheDifference("", "y"))          # 'y'
```

## Solution 2

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sum(ord(c) for c in s)
        b = sum(ord(c) for c in t)
        return chr(b - a)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde")) # e
    print(sol.findTheDifference("", "y")) # y
```
