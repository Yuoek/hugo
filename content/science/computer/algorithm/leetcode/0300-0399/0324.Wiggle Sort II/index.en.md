---
title: 0324.Wiggle Sort II
date: 2026-09-16
---

## Solution

```python
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        n = len(arr)
        i, j = (n - 1) >> 1, n - 1
        for k in range(n):
            if k % 2 == 0:
                nums[k] = arr[i]
                i -= 1
            else:
                nums[k] = arr[j]
                j -= 1

if __name__ == "__main__":
    sol = Solution()
    test1 = [1,5,1,1,6,4]
    sol.wiggleSort(test1)
    print(test1) # [1,6,1,5,1,4]
    test2 = [1,3,2,2,3,1]
    sol.wiggleSort(test2)
    print(test2) # [2,3,1,3,1,2]
```

## Solution 2

```python
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 5001
        for v in nums:
            bucket[v] += 1
        n = len(nums)
        j = 5000
        # 先填奇数位：1,3,5... 放大数
        for i in range(1, n, 2):
            while bucket[j] == 0:
                j -= 1
            nums[i] = j
            bucket[j] -= 1
        # 再填偶数位：0,2,4... 放小数
        for i in range(0, n, 2):
            while bucket[j] == 0:
                j -= 1
            nums[i] = j
            bucket[j] -= 1

if __name__ == "__main__":
    sol = Solution()
    test1 = [1,5,1,1,6,4]
    sol.wiggleSort(test1)
    print(test1) # [1,6,1,5,1,4]
    test2 = [1,3,2,2,3,1]
    sol.wiggleSort(test2)
    print(test2) # [2,3,1,3,1,2]
```
