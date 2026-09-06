---
title: 0189 轮转数组
date: 2026-09-06
---

## Solution

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1

        n = len(nums)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,4,5,6,7]
    sol.rotate(arr,3)
    print(arr)
```
