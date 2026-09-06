---
title: 0071 简化路径
date: 2026-08-16
weight: 71
summary: 栈
---

## Solution

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for s in path.split('/'):
            if not s or s == '.':
                continue
            if s == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(s)
        return '/' + '/'.join(stk)

if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/home/"))               # "/home"
    print(sol.simplifyPath("/../"))                 # "/"
    print(sol.simplifyPath("/home//foo/"))          # "/home/foo"
    print(sol.simplifyPath("/a/./b/../../c/"))      # "/c"
    print(sol.simplifyPath("/a/../../b/../c//.//")) # "/c"

```
