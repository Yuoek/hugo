---
title: 0169 多数元素
date: 2026-09-05
---

## Solution

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = m = 0
        for x in nums:
            if cnt == 0:
                m, cnt = x, 1
            else:
                cnt += 1 if m == x else -1
        return m

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([2,2,1,1,1,2,2]))
```
