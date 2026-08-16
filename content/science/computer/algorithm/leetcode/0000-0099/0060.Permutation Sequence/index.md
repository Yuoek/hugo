---
title: 0060 第 K 个区间排列
date: 2026-08-16
weight: 60
summary: lc
---

## Solution

```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        vis = [False] * (n + 1)
        for i in range(n):
            fact = 1
            for j in range(1, n - i):
                fact *= j
            for j in range(1, n + 1):
                if not vis[j]:
                    if k > fact:
                        k -= fact
                    else:
                        ans.append(str(j))
                        vis[j] = True
                        break
        return ''.join(ans)

if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(3, 3))
    print(sol.getPermutation(4, 9))

```
