---
title: 0376 摆动序列
date: 2026-09-18
---

## Solution

```python
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        f = [1] * n  # f[i]: 以i结尾，最后一步上升的最长摆动子序列长度
        g = [1] * n  # g[i]: 以i结尾，最后一步下降的最长摆动子序列长度
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], g[j] + 1)
                elif nums[j] > nums[i]:
                    g[i] = max(g[i], f[j] + 1)
            ans = max(ans, f[i], g[i])
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.wiggleMaxLength([1,7,4,9,2,5])) # 6
    print(sol.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])) #7
    print(sol.wiggleMaxLength([1,2,3,4,5,6,7,8,9])) #2
```
