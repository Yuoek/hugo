---
title: 0331.Verify Preorder Serialization of a Binary Tree
date: 2026-09-17
---

## Solution

```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stk = []
        for c in preorder.split(","):
            stk.append(c)
            # 当最后三个是 [数字, #, #]，合并成一个#
            while len(stk) > 2 and stk[-1] == stk[-2] == "#" and stk[-3] != "#":
                stk = stk[:-3]
                stk.append("#")
        return len(stk) == 1 and stk[0] == "#"

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")) # True
    print(sol.isValidSerialization("1,#")) # False
    print(sol.isValidSerialization("9,#,#,1")) # False
```
