---
title: 0137.Single Number II
date: 2026-09-04
---

## Solution

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum(num >> i & 1 for num in nums)
            if cnt % 3:
                if i == 31:
                    ans -= 1 << i
                else:
                    ans |= 1 << i
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,3,2]))       # 3
    print(sol.singleNumber([0,1,0,1,0,1,99])) # 99
    print(sol.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])) # -4
```

## Solution 2

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for c in nums:
            aa = (~a & b & c) | (a & ~b & ~c)
            bb = ~a & (b ^ c)
            a, b = aa, bb
        return b


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,3,2]))                 # 3
    print(sol.singleNumber([0,1,0,1,0,1,99]))          # 99
    print(sol.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])) # -4
```
