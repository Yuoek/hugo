---
title: 0043 字符串相乘
date: 2026-08-15
weight: 43
summary: lc
---

## Solution

```python
from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        arr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            a = int(num1[i])
            for j in range(n - 1, -1, -1):
                b = int(num2[j])
                arr[i + j + 1] += a * b
        for i in range(m + n - 1, 0, -1):
            arr[i - 1] += arr[i] // 10
            arr[i] %= 10
        i = 0 if arr[0] else 1
        return "".join(str(x) for x in arr[i:])

if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2", "3"))      # "6"
    print(sol.multiply("123", "456"))  # "56088"
    print(sol.multiply("0", "12345"))  # "0"

```
