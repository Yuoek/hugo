---
title: 0165.Compare Version Numbers
date: 2026-09-05
---

## Solution

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i = j = 0
        while i < m or j < n:
            a = b = 0
            while i < m and version1[i] != '.':
                a = a * 10 + int(version1[i])
                i += 1
            while j < n and version2[j] != '.':
                b = b * 10 + int(version2[j])
                j += 1
            if a != b:
                return -1 if a < b else 1
            i, j = i + 1, j + 1
        return 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion("1.01", "1.001"))
    print(sol.compareVersion("1.0", "1.0.0"))
    print(sol.compareVersion("0.1", "1.1"))
```
