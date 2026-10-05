---
title: 0387.First Unique Character in a String
date: 2026-09-18
---

## Solution

```python
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))     # 0
    print(sol.firstUniqChar("loveleetcode")) # 2
    print(sol.firstUniqChar("aabb"))         # -1
```
