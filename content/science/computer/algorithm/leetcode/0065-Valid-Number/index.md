---
title: 0065 有效数字
date: 2026-08-16
weight: 65
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        i = 0
        if s[i] in '+-':
            i += 1
        if i == n:
            return False
        if s[i] == '.' and (i + 1 == n or s[i + 1] in 'eE'):
            return False
        dot = e = 0
        j = i
        while j < n:
            if s[j] == '.':
                if e or dot:
                    return False
                dot += 1
            elif s[j] in 'eE':
                if e or j == i or j == n - 1:
                    return False
                e += 1
                if s[j + 1] in '+-':
                    j += 1
                    if j == n - 1:
                        return False
            elif not s[j].isnumeric():
                return False
            j += 1
        return True

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("2", True), ("0089", True), ("-0.1", True), ("+3.14", True),
        ("4.", True), ("-.9", True), ("2e10", True), ("-90E3", True),
        ("3e+7", True), ("+6e-1", True), ("53.5e93", True), ("-123.456e789", True),
        ("abc", False), ("1a", False), ("1e", False), ("e3", False),
        ("--6", False), ("-+3", False), ("95a54e53", False),
        (".", False), (".e1", False), ("+.", False)
    ]
    for s, expect in test_cases:
        res = sol.isNumber(s)
        print(f"{s!r} → {res}, expect {expect} {'OK' if res==expect else 'FAIL'}")

```
