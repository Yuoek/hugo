---
title: 0084 柱状图中最大的矩形
date: 2026-08-17
weight: 84
summary: 单调栈
---

## Solution

```python
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        left = [-1] * n
        right = [n] * n
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3])) # 10

```
