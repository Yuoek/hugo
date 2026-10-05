---
title: 0395 至少有 K 个重复字符的最长子串
date: 2026-09-18
---

## Solution

```python
from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(l, r):
            cnt = Counter(s[l : r + 1])
            split = next((c for c, v in cnt.items() if v < k), '')
            if not split:
                return r - l + 1
            i = l
            ans = 0
            while i <= r:
                while i <= r and s[i] == split:
                    i += 1
                if i >= r:
                    break
                j = i
                while j <= r and s[j] != split:
                    j += 1
                t = dfs(i, j - 1)
                ans = max(ans, t)
                i = j
            return ans

        return dfs(0, len(s) - 1)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubstring("aaabb", 3))      # 3
    print(sol.longestSubstring("ababbc", 2))    # 5
    print(sol.longestSubstring("a", 1))         # 1
```
