---
title: 0093 复制 IP 地址
date: 2026-08-17
weight: 93
summary: 回溯
---

## Solution

```python
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(i: int, j: int) -> bool:
            if s[i] == "0" and i != j:
                return False
            return 0 <= int(s[i : j + 1]) <= 255

        def dfs(i: int):
            if i >= n and len(t) == 4:
                ans.append(".".join(t))
                return
            if i >= n or len(t) >= 4:
                return
            for j in range(i, min(i + 3, n)):
                if check(i, j):
                    t.append(s[i : j + 1])
                    dfs(j + 1)
                    t.pop()

        n = len(s)
        ans = []
        t = []
        dfs(0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
    # ['255.255.11.135','255.255.111.35']
    print(sol.restoreIpAddresses("0000"))
    # ['0.0.0.0']

```
