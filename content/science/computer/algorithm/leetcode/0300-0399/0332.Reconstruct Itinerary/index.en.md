---
title: 0332.Reconstruct Itinerary
date: 2026-09-17
---

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(f: str):
            while g[f]:
                dfs(g[f].pop())
            ans.append(f)

        g = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            g[f].append(t)
        ans = []
        dfs("JFK")
        return ans[::-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    # ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
    print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    # ['JFK','ATL','JFK','SFO','ATL','SFO']
```
