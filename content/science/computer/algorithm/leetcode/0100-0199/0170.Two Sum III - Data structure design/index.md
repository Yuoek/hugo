---
title: 0170 两数之和 III - 数据结构设计
date: 2026-09-05
---

## Solution

```python
from collections import defaultdict

class TwoSum:

    def __init__(self):
        self.cnt = defaultdict(int)

    def add(self, number: int) -> None:
        self.cnt[number] += 1

    def find(self, value: int) -> bool:
        for x, v in self.cnt.items():
            y = value - x
            if y in self.cnt and (x != y or v > 1):
                return True
        return False

if __name__ == "__main__":
    ts = TwoSum()
    ts.add(1)
    ts.add(3)
    ts.add(5)
    print(ts.find(4))
    print(ts.find(7))
```
