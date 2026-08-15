---
title: 0042 接雨水
date: 2026-08-15
weight: 42
summary: 双指针
---

## Solution

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [height[0]] * n
        right = [height[-1]] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            right[n - i - 1] = max(right[n - i], height[n - i - 1])
        return sum(min(l, r) - h for l, r, h in zip(left, right, height))

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(sol.trap([4,2,0,3,2,5]))             # 9

```
