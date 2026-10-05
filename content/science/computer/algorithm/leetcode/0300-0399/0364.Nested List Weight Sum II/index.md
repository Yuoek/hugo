---
titel: 0364 嵌套列表加权和 II
date: 2026-09-18
---

## Solution

```python
from typing import List
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       if value is not None:
           self._val = value
           self._list = None
       else:
           self._val = None
           self._list = []
   def isInteger(self):
       return self._val is not None
   def add(self, elem):
       self._list.append(elem)
   def setInteger(self, value):
       self._val = value
       self._list = None
   def getInteger(self):
       return self._val
   def getList(self):
       return self._list

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def dfs(x, d):
            nonlocal maxDepth, s, ws
            maxDepth = max(maxDepth, d)
            if x.isInteger():
                s += x.getInteger()
                ws += x.getInteger() * d
            else:
                for y in x.getList():
                    dfs(y, d + 1)

        maxDepth = s = ws = 0
        for x in nestedList:
            dfs(x, 1)
        return (maxDepth + 1) * s - ws

# 本地测试
if __name__ == "__main__":
    # 构造样例 [[1,1],2,[1,1]]
    n1 = NestedInteger()
    n1.add(NestedInteger(1))
    n1.add(NestedInteger(1))
    n2 = NestedInteger(2)
    n3 = NestedInteger()
    n3.add(NestedInteger(1))
    n3.add(NestedInteger(1))
    lst = [n1, n2, n3]
    sol = Solution()
    print(sol.depthSumInverse(lst)) # 8

    # 样例 [1,[4,[6]]]
    a1 = NestedInteger(1)
    a2 = NestedInteger()
    a2.add(NestedInteger(4))
    a3 = NestedInteger()
    a3.add(NestedInteger(6))
    a2.add(a3)
    lst2 = [a1, a2]
    print(sol.depthSumInverse(lst2)) # 17
```
