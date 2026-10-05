---
title: 0345.Reverse Vowels of a String
date: 2026-09-17
---

## Solution

```python
from typing import str

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        cs = list(s)
        while i < j:
            while i < j and cs[i] not in vowels:
                i += 1
            while i < j and cs[j] not in vowels:
                j -= 1
            if i < j:
                cs[i], cs[j] = cs[j], cs[i]
                i, j = i + 1, j - 1
        return "".join(cs)

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels("hello"))    # "holle"
    print(sol.reverseVowels("leetcode")) # "leotcede"
    print(sol.reverseVowels("aA"))       # "Aa"
    print(sol.reverseVowels("xyz"))      # "xyz"
```
