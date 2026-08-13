---
title: 0013-罗马数字转整数
date: 2026-08-13
weight: 13
summary: 罗马数字规则
---

## Solution

```python
from itertools import pairwise

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0
        n = len(s)
        for i in range(n-1):
           ds = d[s[i]]
            dsp = d[s[i+1]]
            if d[s[i]] < d[s[i+1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        res += d[s[-1]]

        return sum((-1 if d[a] < d[b] else 1) * d[a] for a, b in pairwise(s)) + d[s[-1]]

if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))      # 3
    print(sol.romanToInt("IV"))       # 4
    print(sol.romanToInt("IX"))       # 9
    print(sol.romanToInt("LVIII"))    # 58
    print(sol.romanToInt("MCMXCIV"))  # 1994

```

大数在左边乘 1
小数在左边乘 -1
最后和最后的数相加
