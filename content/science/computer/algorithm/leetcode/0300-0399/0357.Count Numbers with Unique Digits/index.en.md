---
title: 0357.Count Numbers with Unique Digits
date: 2026-09-18
---

## Solution

```python
from functools import cache

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @cache
        def dfs(i: int, mask: int, lead: bool) -> int:
            if i < 0:
                return 1
            ans = 0
            for j in range(10):
                if mask >> j & 1:
                    continue
                if lead and j == 0:
                    ans += dfs(i - 1, mask, True)
                else:
                    ans += dfs(i - 1, mask | 1 << j, False)
            return ans

        return dfs(n - 1, 0, True)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.countNumbersWithUniqueDigits(0)) # 1
    print(sol.countNumbersWithUniqueDigits(1)) # 10
    print(sol.countNumbersWithUniqueDigits(2)) # 91
    print(sol.countNumbersWithUniqueDigits(3)) # 739
```
