---
title: 0187.Repeated DNA Sequences
date: 2026-09-06
---

## Solution

```python
from typing import List
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = Counter()
        ans = []
        for i in range(len(s) - 10 + 1):
            t = s[i : i + 10]
            cnt[t] += 1
            if cnt[t] == 2:
                ans.append(t)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
```
