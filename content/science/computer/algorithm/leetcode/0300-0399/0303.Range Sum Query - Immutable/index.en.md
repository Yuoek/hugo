---
title: 0303.Range Sum Query - Immutable
date: 2026-09-09
---

## Sulotion

```python
from typing import List
from itertools import accumulate

class NumArray:
    def __init__(self, nums: List[int]):
        self.s = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]


if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2)) # 1
    print(obj.sumRange(2, 5)) # -1
    print(obj.sumRange(0, 5)) # -3
```
