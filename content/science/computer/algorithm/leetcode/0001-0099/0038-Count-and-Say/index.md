---
title: 0038 外观数列
date: 2026-08-14
weight: 38
summary: 双指针
---

## Solution

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            i = 0
            t = []
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                t.append(str(j - i))
                t.append(str(s[i]))
                i = j
            s = ''.join(t)
        return s

if __name__ == "__main__":
    sol = Solution()
    for x in range(1, 6):
        print(x, sol.countAndSay(x))
    # 1:"1"
    # 2:"11"
    # 3:"21"
    # 4:"1211"
    # 5:"111221"

```
