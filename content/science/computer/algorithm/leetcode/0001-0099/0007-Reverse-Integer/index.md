---
title: 0007 整数反转
date: 2026-08-12
weight: 8
summary: 思想
---

## Solution

```python
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        mi, mx = -(2**31), 2**31 - 1
        while x:
            if ans < mi // 10 + 1 or ans > mx // 10:
                return 0
            y = x % 10
            if x < 0 and y > 0:
                y -= 10
            ans = ans * 10 + y
            x = (x - y) // 10
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(120))
    print(sol.reverse(0))
    print(sol.reverse(1534236469)) 
    
```

`边界限制`
`负数取模`

