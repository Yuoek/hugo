---
title: 0340 至多包含 K 个不同字符的最长子串 
date: 2026-09-17
---

## Solution

```python
from typing import str
from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        cnt = Counter()
        for c in s:
            cnt[c] += 1
            if len(cnt) > k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
        return len(s) - l

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))    # 3
    print(sol.lengthOfLongestSubstringKDistinct("aa", 1))       # 2
    print(sol.lengthOfLongestSubstringKDistinct("abcabc", 2))   # 2
```
