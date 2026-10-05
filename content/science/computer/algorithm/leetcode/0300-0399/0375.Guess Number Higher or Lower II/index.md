---
title: 0375 猜数字大小 II
date: 2026-09-18
---

## Solution

```python
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = j + f[i][j - 1]
                for k in range(i, j):
                    f[i][j] = min(f[i][j], max(f[i][k - 1], f[k + 1][j]) + k)
        return f[1][n]

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.getMoneyAmount(10)) # 16
    print(sol.getMoneyAmount(1))  # 0
    print(sol.getMoneyAmount(2))  # 1
```
