---
title: 0321 拼接最大数
date: 2026-09-16
---

## Solution

```python
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def f(nums: List[int], k: int) -> List[int]:
            n = len(nums)
            stk = [0] * k
            top = -1
            remain = n - k
            for x in nums:
                while top >= 0 and stk[top] < x and remain > 0:
                    top -= 1
                    remain -= 1
                if top + 1 < k:
                    top += 1
                    stk[top] = x
                else:
                    remain -= 1
            return stk

        def compare(nums1: List[int], nums2: List[int], i: int, j: int) -> bool:
            if i >= len(nums1):
                return False
            if j >= len(nums2):
                return True
            if nums1[i] > nums2[j]:
                return True
            if nums1[i] < nums2[j]:
                return False
            return compare(nums1, nums2, i + 1, j + 1)

        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            m, n = len(nums1), len(nums2)
            i = j = 0
            ans = [0] * (m + n)
            for idx in range(m + n):
                if compare(nums1, nums2, i, j):
                    ans[idx] = nums1[i]
                    i += 1
                else:
                    ans[idx] = nums2[j]
                    j += 1
            return ans

        m, n = len(nums1), len(nums2)
        l, r = max(0, k - n), min(k, m)
        ans = [0] * k
        for x in range(l, r + 1):
            arr1 = f(nums1, x)
            arr2 = f(nums2, k - x)
            arr = merge(arr1, arr2)
            if ans < arr:
                ans = arr
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5)) # [9,8,6,5,3]
    print(sol.maxNumber([6,7], [6,0,4], 5))            # [6,7,6,0,4]
    print(sol.maxNumber([3,9], [8,9], 3))             # [9,8,9]
```
