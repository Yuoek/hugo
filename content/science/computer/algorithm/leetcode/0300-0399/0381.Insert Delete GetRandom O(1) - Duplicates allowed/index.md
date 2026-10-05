---
title: 0381 O(1) 时间插入、删除和获取随机元素 - 允许重复
date: 2026-09-18
---

## Solution

```python
import random

class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}
        self.l = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        idx_set = self.m.get(val, set())
        idx_set.add(len(self.l))
        self.m[val] = idx_set
        self.l.append(val)
        return len(idx_set) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.m:
            return False
        idx_set = self.m[val]
        idx = next(iter(idx_set))
        last_idx = len(self.l) - 1
        self.l[idx] = self.l[last_idx]
        idx_set.remove(idx)

        last_val = self.l[last_idx]
        last_idx_set = self.m[last_val]
        last_idx_set.remove(last_idx)
        if idx < last_idx:
            last_idx_set.add(idx)
        if not idx_set:
            self.m.pop(val)
        self.l.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.l)

# 本地测试
if __name__ == "__main__":
    obj = RandomizedCollection()
    print(obj.insert(1)) # True
    print(obj.insert(1)) # False
    print(obj.insert(2)) # True
    print(obj.getRandom()) # 1/2
    print(obj.remove(1))  # True
    print(obj.getRandom()) #1/2
```
