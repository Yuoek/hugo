---
title: 0032 最长有效括号
date: 2026-08-14
weight: 32
summary: DP
---

## Solution

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        for i, c in enumerate(s, 1):
            if c == ")":
                if i > 1 and s[i - 2] == "(":
                    f[i] = f[i - 2] + 2
                else:
                    j = i - f[i - 1] - 1
                    if j and s[j - 1] == "(":
                        f[i] = f[i - 1] + 2 + f[j - 1]
        return max(f)

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses("(()"))      # 2
    print(sol.longestValidParentheses(")()())"))   # 4
    print(sol.longestValidParentheses(""))          # 0
    print(sol.longestValidParentheses("()(())"))    # 6

```
