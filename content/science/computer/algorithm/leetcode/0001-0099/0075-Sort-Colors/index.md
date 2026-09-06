---
title: 0075 颜色分类
date: 2026-08-17
weight: 75
summary: 三指针
---

## Solution

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = -1, len(nums), 0
        while k < j:
            if nums[k] == 0:
                i += 1
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
            elif nums[k] == 2:
                j -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                k += 1

if __name__ == "__main__":
    sol = Solution()
    arr = [2,0,2,1,1,0]
    sol.sortColors(arr)
    print(arr) # [0, 0, 1, 1, 2, 2]

```
