---
title: 0385.Mini Parser
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
    def deserialize(self, s: str) -> NestedInteger:
        if not s or s == '[]':
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        ans = NestedInteger()
        depth, j = 0, 1
        for i in range(1, len(s)):
            if depth == 0 and (s[i] == ',' or i == len(s) - 1):
                ans.add(self.deserialize(s[j:i]))
                j = i + 1
            elif s[i] == '[':
                depth += 1
            elif s[i] == ']':
                depth -= 1
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    res1 = sol.deserialize("[1,2,3]")
    print(res1.getList()[0].getInteger()) #1

    res2 = sol.deserialize("[1,[2,3],4]")
    print(res2.getList()[1].getList()[1].getInteger()) #3

    res3 = sol.deserialize("123")
    print(res3.getInteger()) #123
```

## Solution 2

```python
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
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stk, x, neg = [], 0, False
        for i, c in enumerate(s):
            if c == '-':
                neg = True
            elif c.isdigit():
                x = x * 10 + int(c)
            elif c == '[':
                stk.append(NestedInteger())
            elif c in ',]':
                if s[i - 1].isdigit():
                    if neg:
                        x = -x
                    stk[-1].add(NestedInteger(x))
                x, neg = 0, False
                if c == ']' and len(stk) > 1:
                    t = stk.pop()
                    stk[-1].add(t)
        return stk.pop()

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    res1 = sol.deserialize("[1,2,3]")
    print(res1.getList()[0].getInteger()) #1
    res2 = sol.deserialize("[1,[2,-3],4]")
    print(res2.getList()[1].getList()[1].getInteger()) # -3
    res3 = sol.deserialize("123")
    print(res3.getInteger()) #123

```
