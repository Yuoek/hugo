---
title: 0352 将数据流变为多个不相交区间
date: 2026-09-18
---

## Solution

```python
from typing import List
from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self):
        self.mp = SortedDict()

    def addNum(self, val: int) -> None:
        n = len(self.mp)
        ridx = self.mp.bisect_right(val)
        lidx = n if ridx == 0 else ridx - 1
        keys = self.mp.keys()
        values = self.mp.values()
        if (
            lidx != n
            and ridx != n
            and values[lidx][1] + 1 == val
            and values[ridx][0] - 1 == val
        ):
            # 合并左右两个区间
            self.mp[keys[lidx]][1] = self.mp[keys[ridx]][1]
            self.mp.pop(keys[ridx])
        elif lidx != n and val <= values[lidx][1] + 1:
            # 接上左边区间
            self.mp[keys[lidx]][1] = max(val, self.mp[keys[lidx]][1])
        elif ridx != n and val >= values[ridx][0] - 1:
            # 接上右边区间
            self.mp[keys[ridx]][0] = min(val, self.mp[keys[ridx]][0])
        else:
            # 新建独立区间
            self.mp[val] = [val, val]

    def getIntervals(self) -> List[List[int]]:
        return list(self.mp.values())

# 本地测试
if __name__ == "__main__":
    obj = SummaryRanges()
    obj.addNum(1)
    print(obj.getIntervals()) # [[1,1]]
    obj.addNum(3)
    print(obj.getIntervals()) # [[1,1],[3,3]]
    obj.addNum(2)
    print(obj.getIntervals()) # [[1,3]]
    obj.addNum(7)
    obj.addNum(6)
    print(obj.getIntervals()) # [[1,3],[6,7]]

```
