---
title: 0368.Largest Divisible Subset
date: 2026-09-18
---

## Solution

```python
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        f = [1] * n
        k = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    f[i] = max(f[i], f[j] + 1)
            if f[k] < f[i]:
                k = i
        m = f[k]
        i = k
        ans = []
        while m:
            if nums[k] % nums[i] == 0 and f[i] == m:
                ans.append(nums[i])
                k, m = i, m - 1
            i -= 1
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestDivisibleSubset([1,2,3])) # [2,1] or [3,1]
    print(sol.largestDivisibleSubset([1,2,4,8])) # [8,4,2,1]
    print(sol.largestDivisibleSubset([3,4,16,8])) # [16,8,4]
```
