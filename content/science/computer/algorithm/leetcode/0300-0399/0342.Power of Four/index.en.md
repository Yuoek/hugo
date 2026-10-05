---
title: 0342.Power of Four
date: 2026-09-17
---

## Solution

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfFour(16))  # True
    print(sol.isPowerOfFour(5))   # False
    print(sol.isPowerOfFour(1))   # True
    print(sol.isPowerOfFour(8))   # False
    print(sol.isPowerOfFour(0))   # False
```
