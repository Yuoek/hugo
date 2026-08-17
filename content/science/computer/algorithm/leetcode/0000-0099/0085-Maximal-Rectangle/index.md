---
title: 0085 最大矩形
date: 2026-08-17
weight: 85
summary: 单调栈
---

## Solution

```python
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        ans = 0
        for row in matrix:
            for j, v in enumerate(row):
                if v == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        left = [-1] * n
        right = [n] * n
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while stk and heights[stk[-1]] >= h:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))

if __name__ == "__main__":
    sol = Solution()
    mat = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print(sol.maximalRectangle(mat)) # 6

```
