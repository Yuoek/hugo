---
title: 0377 组合总和 Ⅳ
date: 2026-09-18
---

## Solution

```python
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        f = [1] + [0] * target
        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    f[i] += f[i - x]
        return f[target]

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum4([1,2,3], 4)) # 7
    print(sol.combinationSum4([9], 3)) # 0
```
