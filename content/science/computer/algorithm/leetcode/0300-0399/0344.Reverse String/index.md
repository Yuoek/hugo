---
title: 0344 反转字符串
date: 2026-09-17
---

## Solution

```python
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1

if __name__ == "__main__":
    sol = Solution()
    arr1 = ["h","e","l","l","o"]
    sol.reverseString(arr1)
    print(arr1) # ['o','l','l','e','h']

    arr2 = ["H","a","n","n","a","h"]
    sol.reverseString(arr2)
    print(arr2) # ['h','a','n','n','a','H']
```
