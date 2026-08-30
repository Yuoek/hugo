---
title: 0089 格雷编码
date: 2026-08-17
weight: 89
summary: 公式
---

## Solution

```python
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.grayCode(2)) # [0,1,3,2]
    print(sol.grayCode(3)) # [0,1,3,2,6,7,5,4]

```
