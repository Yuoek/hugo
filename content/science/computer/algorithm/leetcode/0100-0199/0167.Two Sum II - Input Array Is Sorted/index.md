---
title: 0167 两数之和 II - 输入有序数组
date: 2026-09-05
---

## Solution

```python
from typing import List
import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            x = target - numbers[i]
            j = bisect_left(numbers, x, lo=i + 1)
            if j < n and numbers[j] == x:
                return [i + 1, j + 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([2,3,4],6))
```

## Solution 2

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            x = numbers[i] + numbers[j]
            if x == target:
                return [i + 1, j + 1]
            if x < target:
                i += 1
            else:
                j -= 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([2,3,4],6))
    print(sol.twoSum([-1,0],-1))
```
