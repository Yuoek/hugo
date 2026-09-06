---
title: 0045 跳跃游戏
date: 2026-08-15
weight: 45
summary: 贪心
---

## Solution

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = mx = last = 0
        for i, x in enumerate(nums[:-1]):
            mx = max(mx, i + x)
            if last == i:
                ans += 1
                last = mx
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([2,3,1,1,4])) # 2
    print(sol.jump([2,1]))       # 1
    print(sol.jump([1]))         # 0

```

到达边界加1。
