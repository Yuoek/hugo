---
title: 0066 加一
date: 2026-08-16
weight: 66
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        return [1] + digits

# test
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1,2,3]))
    print(sol.plusOne([9,9,9]))

```

原地修改
