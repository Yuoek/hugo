---
title: 0398.Random Pick Index
date: 2026-09-18
---

## Solution

```python
import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        n = ans = 0
        for i, v in enumerate(self.nums):
            if v == target:
                n += 1
                x = random.randint(1, n)
                if x == n:
                    ans = i
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# 本地测试
if __name__ == "__main__":
    obj = Solution([1,2,3,3,3])
    print([obj.pick(3) for _ in range(10)]) # 2,3,4 等概率
```
