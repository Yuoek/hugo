---
title: 0049 字母异位词分组
date: 2026-08-15
weight: 49
summary: 哈希
---

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            d[k].append(s)
        return list(d.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # [["eat","tea","ate"],["tan","nat"],["bat"]]
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))

```
