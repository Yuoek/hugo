---
title: 0009 回文数
date: 2026-08-13
weight: 9
summary: 模
---

## Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and x % 10 == 0):
            return False
        y = 0
        while y < x:
            y = y * 10 + x % 10
            x //= 10
        return x in (y, y // 10)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # True
    print(sol.isPalindrome(-121))  # False
    print(sol.isPalindrome(10))    # False
    print(sol.isPalindrome(12321)) # True
    print(sol.isPalindrome(0))     # True

```
