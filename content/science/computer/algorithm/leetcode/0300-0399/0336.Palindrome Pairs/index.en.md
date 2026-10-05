---
title: 0336.Palindrome Pairs
date: 2026-09-17
---

## Solution

```python
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {w: i for i, w in enumerate(words)}
        ans = []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                a, b = w[:j], w[j:]
                ra, rb = a[::-1], b[::-1]
                # w=a+b，b是回文，找ra放在前面：ra + a+b = ra + w
                if ra in d and d[ra] != i and b == rb:
                    ans.append([i, d[ra]])
                # j>0避免重复，a是回文，找rb放在后面：a+b + rb = w + rb
                if j and rb in d and d[rb] != i and a == ra:
                    ans.append([d[rb], i])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))
    # [[0,1],[1,0],[3,2],[2,4]]
    print(sol.palindromePairs(["bat","tab","cat"]))
    # [[0,1],[1,0]]
```
