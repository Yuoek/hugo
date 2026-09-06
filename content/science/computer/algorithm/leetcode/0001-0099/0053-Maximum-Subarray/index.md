---
titel: 0053 最大子数组和
date: 2026-08-16
weight: 53
summary: DP
---

## Solution

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = f = nums[0]
        for x in nums[1:]:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(sol.maxSubArray([5,4,-1,7,8]))

```
