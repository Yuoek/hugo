---
title: 0318 最大单词长度乘积
date: 2026-09-16
---

## Solution

```python
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [0] * len(words)
        ans = 0
        for i, s in enumerate(words):
            for c in s:
                mask[i] |= 1 << (ord(c) - ord("a"))
            for j, t in enumerate(words[:i]):
                if (mask[i] & mask[j]) == 0:
                    ans = max(ans, len(s) * len(t))
        return ans

if __name__ == "__main__":
    sol = Solution()
    # test case1
    words1 = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print(sol.maxProduct(words1)) # expect 16
    # test case2
    words2 = ["a","ab","abc","d","cd","bcd","abcd"]
    print(sol.maxProduct(words2)) # expect 4
    # test case3
    words3 = ["a","aa","aaa","aaaa"]
    print(sol.maxProduct(words3)) # expect 0
```

## Solution 2

```python
from typing import List
from collections import defaultdict

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = defaultdict(int)
        ans = 0
        for s in words:
            a = len(s)
            x = 0
            for c in s:
                x |= 1 << (ord(c) - ord("a"))
            for y, b in mask.items():
                if (x & y) == 0:
                    ans = max(ans, a * b)
            mask[x] = max(mask[x], a)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))  # 16
    print(sol.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))      # 4
    print(sol.maxProduct(["a","aa","aaa","aaaa"]))                      # 0
```
