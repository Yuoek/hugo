---
title: 0374 猜数字大小
date: 2026-09-18
---

## Solution

```python
import bisect

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect.bisect(range(1, n + 1), 0, key=lambda x: -guess(x))

# ====== 本地测试代码（实现guess模拟API）======
if __name__ == "__main__":
    pick = 6
    def guess(num: int) -> int:
        if num > pick:
            return -1
        elif num < pick:
            return 1
        else:
            return 0

    sol = Solution()
    print(sol.guessNumber(10)) # expected 6
```
