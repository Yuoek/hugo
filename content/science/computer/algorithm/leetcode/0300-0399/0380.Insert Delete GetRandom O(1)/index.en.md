---
title: 0380.Insert Delete GetRandom O(1)
date: 2026-09-18
---

## Solution

```python
import random
from random import choice

class RandomizedSet:
    def __init__(self):
        self.d = {}
        self.q = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.q)
        self.q.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        i = self.d[val]
        # 将最后一个元素移到被删除位置
        self.d[self.q[-1]] = i
        self.q[i] = self.q[-1]
        self.q.pop()
        self.d.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.q)

# 本地测试
if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))  # True
    print(obj.remove(2))  # False
    print(obj.insert(2))  # True
    print(obj.getRandom())# 1 or 2
    print(obj.remove(1))  # True
    print(obj.insert(2))  # False
    print(obj.getRandom())# 2
```
