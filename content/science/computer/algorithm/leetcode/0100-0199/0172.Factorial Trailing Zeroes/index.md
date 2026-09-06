---
title: 0172 阶乘后的零
date: 2026-09-05
---

## Solution

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(3))
    print(sol.trailingZeroes(5))
    print(sol.trailingZeroes(25))
```
