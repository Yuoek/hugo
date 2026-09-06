---
title: 0168 Excel 列表排名
date: 2026-09-05
---

## Solution

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            res.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(res[::-1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToTitle(1))
    print(sol.convertToTitle(28))
    print(sol.convertToTitle(701))
```
