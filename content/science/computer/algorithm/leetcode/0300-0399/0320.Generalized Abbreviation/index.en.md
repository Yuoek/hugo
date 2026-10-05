---
title: 0320.Generalized Abbreviation
date: 2026-09-16
---

## Solution

```python
from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(i: int) -> List[str]:
            if i >= n:
                return [""]
            # 不缩写当前字符，直接保留word[i]
            ans = [word[i] + s for s in dfs(i + 1)]
            # 从i开始，缩写长度 j-i 的字符
            for j in range(i + 1, n + 1):
                for s in dfs(j + 1):
                    suffix = word[j] if j < n else ""
                    ans.append(str(j - i) + suffix + s)
            return ans

        n = len(word)
        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateAbbreviations("word"))
```

## Solution 2

```python
from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        ans = []
        for i in range(1 << n):
            cnt = 0
            s = []
            for j in range(n):
                if i >> j & 1:
                    cnt += 1
                else:
                    if cnt:
                        s.append(str(cnt))
                        cnt = 0
                    s.append(word[j])
            if cnt:
                s.append(str(cnt))
            ans.append("".join(s))
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateAbbreviations("word"))
```
