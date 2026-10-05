---
title: 0386.Lexicographical Numbers
date: 2026-09-18
---

## Solution

```python
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        v = 1
        for _ in range(n):
            ans.append(v)
            if v * 10 <= n:
                v *= 10
            else:
                while v % 10 == 9 or v + 1 > n:
                    v //= 10
                v += 1
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.lexicalOrder(13)) # [1,10,11,12,13,2,3,4,5,6,7,8,9]
    print(sol.lexicalOrder(2))  # [1,2]
```
