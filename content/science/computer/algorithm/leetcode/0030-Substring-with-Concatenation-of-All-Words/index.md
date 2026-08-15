---
title: 0030 串连所有单词的子串
date: 2026-08-14
weight: 30
summary: 分组滑动窗口
---

## Solution

```python
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt = Counter(words)
        m, n = len(s), len(words)
        k = len(words[0])
        ans = []
        for i in range(k):
            l = r = i
            cnt1 = Counter()
            while r + k <= m:
                t = s[r : r + k]
                r += k
                if cnt[t] == 0:
                    l = r
                    cnt1.clear()
                    continue
                cnt1[t] += 1
                while cnt1[t] > cnt[t]:
                    rem = s[l : l + k]
                    l += k
                    cnt1[rem] -= 1
                if r - l == n * k:
                    ans.append(l)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))  # [0,9]
    print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])) # []
    print(sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) # [6,9,12]

```
