---
title: 0371 两整数之和
date: 2026-09-18
---

## Solution

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a, b = a & 0xFFFFFFFF, b & 0xFFFFFFFF
        while b:
            carry = ((a & b) << 1) & 0xFFFFFFFF
            a, b = a ^ b, carry
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(1,2))   #3
    print(sol.getSum(-2,3))  #1
    print(sol.getSum(-1,1))  #0
```
