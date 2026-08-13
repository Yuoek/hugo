---
title: 0018 四数之和
date: 2026-08-13
weight: 18
summary: 排序 双层固定 双指针
---

## Solution

```python
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        if n < 4:
            return ans
        nums.sort()
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, n - 1
                while k < l:
                    x = nums[i] + nums[j] + nums[k] + nums[l]
                    if x < target:
                        k += 1
                    elif x > target:
                        l -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k, l = k + 1, l - 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSum([1,0,-1,0,-2,2], 0))    # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(sol.fourSum([2,2,2,2,2], 8))        # [[2,2,2,2]]
    print(sol.fourSum([0,0,0,0], 0))          # [[0,0,0,0]]

```
