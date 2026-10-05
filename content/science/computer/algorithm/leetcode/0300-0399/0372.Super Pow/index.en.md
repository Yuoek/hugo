---
title: 0372.Super Pow
date: 2026-09-18
---

## Solution

```python
from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        ans = 1
        for e in b[::-1]:
            ans = ans * pow(a, e, mod) % mod
            a = pow(a, 10, mod)
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.superPow(2, [3]))          # 8
    print(sol.superPow(2, [1,0]))        # 1024 %1337 = 1024
    print(sol.superPow(1, [4,3,3,8,5,2]))# 1
```
