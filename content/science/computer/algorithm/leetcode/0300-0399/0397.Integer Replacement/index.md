---
title: 0397 整数替换
date: 2026-09-18
---

## Solution

```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n != 1:
            if (n & 1) == 0:
                n >>= 1
            elif n != 3 and (n & 3) == 3:
                n += 1
            else:
                n -= 1
            ans += 1
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.integerReplacement(8))  # 3
    print(sol.integerReplacement(7))  # 4
    print(sol.integerReplacement(3))  # 2
```
