---
title: 0399.Evaluate Division
date: 2026-09-18
---

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        def find(x):
            if p[x] != x:
                origin = p[x]
                p[x] = find(p[x])
                w[x] *= w[origin]
            return p[x]

        w = defaultdict(lambda: 1.0)
        p = dict()
        # 初始化父节点
        for a, b in equations:
            p[a] = a
            p[b] = b
        for i, v in enumerate(values):
            a, b = equations[i]
            pa, pb = find(a), find(b)
            if pa == pb:
                continue
            p[pa] = pb
            w[pa] = w[b] * v / w[a]

        return [
            -1.0 if c not in p or d not in p or find(c) != find(d) else w[c] / w[d]
            for c, d in queries
        ]

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    eq = [["a","b"],["b","c"]]
    val = [2.0,3.0]
    qs = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(sol.calcEquation(eq, val, qs)) # [6.0, 0.5, -1.0, 1.0, -1.0]
```
