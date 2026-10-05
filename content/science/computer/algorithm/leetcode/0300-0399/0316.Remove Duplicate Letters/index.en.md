---
title: 0316.Remove Duplicate Letters
date: 2026-09-10
---

## Solution

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stk = []
        vis = set()
        for i, c in enumerate(s):
            if c in vis:
                continue
            while stk and stk[-1] > c and last[stk[-1]] > i:
                vis.remove(stk.pop())
            stk.append(c)
            vis.add(c)
        return ''.join(stk)

def main():
    sol = Solution()
    print(sol.removeDuplicateLetters("bcabc"))
    print(sol.removeDuplicateLetters("cbacdcbc"))

if __name__ == "__main__":
    main()

```

## Solution 2

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count, in_stack = [0] * 128, [False] * 128
        stack = []
        for c in s:
            count[ord(c)] += 1
        for c in s:
            count[ord(c)] -= 1
            if in_stack[ord(c)]:
                continue
            while len(stack) and stack[-1] > c:
                peek = stack[-1]
                if count[ord(peek)] < 1:
                    break
                in_stack[ord(peek)] = False
                stack.pop()
            stack.append(c)
            in_stack[ord(c)] = True
        return ''.join(stack)

def main():
    sol = Solution()
    print(sol.removeDuplicateLetters("bcabc"))
    print(sol.removeDuplicateLetters("cbacdcbc"))

if __name__ == "__main__":
    main()
```
