---
title: 0362.Design Hit Counter
date: 2026-09-18
---

## Solution

```python
import bisect

class HitCounter:

    def __init__(self):
        self.ts = []

    def hit(self, timestamp: int) -> None:
        self.ts.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return len(self.ts) - bisect.bisect_left(self.ts, timestamp - 300 + 1)

# 本地测试
if __name__ == "__main__":
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    print(obj.getHits(4))   # 3
    obj.hit(300)
    print(obj.getHits(300)) # 4
    print(obj.getHits(301)) # 3
```
