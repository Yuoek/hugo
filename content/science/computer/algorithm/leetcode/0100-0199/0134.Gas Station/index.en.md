---
title: 0134.Gas Station
date: 2026-09-04
---

## Solution

```python
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = j = n - 1
        cnt = s = 0
        while cnt < n:
            s += gas[j] - cost[j]
            cnt += 1
            j = (j + 1) % n
            while s < 0 and cnt < n:
                i -= 1
                s += gas[i] - cost[i]
                cnt += 1
        return -1 if s < 0 else i


if __name__ == "__main__":
    sol = Solution()
    print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
    print(sol.canCompleteCircuit([2,3,4], [3,4,3])) # -1
    print(sol.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])) # 4
```
