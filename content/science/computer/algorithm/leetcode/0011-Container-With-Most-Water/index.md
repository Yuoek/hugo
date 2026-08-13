---
title: 0011 盛最多水的容器
date: 2026-08-13
weight: 11
summary: 双指针
---

## Solution

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))   # 49
    print(s.maxArea([1,1]))                 # 1
    print(s.maxArea([4,3,2,1,4]))           # 16

```
