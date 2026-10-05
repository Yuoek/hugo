---
title: 0338 比特位计数
date: 2026-09-17
---

## Solution

```python
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(5)) # [0,1,1,2,1,2]
```

## Solution 2

```python
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(5)) # [0,1,1,2,1,2]
```
