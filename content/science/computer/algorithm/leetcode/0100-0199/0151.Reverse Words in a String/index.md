---
title: 0151 反转字符串中的单词
date: 2026-09-05
---

## Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i, n = 0, len(s)
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i < n:
                j = i
                while j < n and s[j] != " ":
                    j += 1
                words.append(s[i:j])
                i = j
        return " ".join(words[::-1])

if __name__ == "__main__":
    sol = Solution()
    print(repr(sol.reverseWords("the sky is blue")))
    print(repr(sol.reverseWords("  hello world  ")))
    print(repr(sol.reverseWords("a good   example")))
```

## Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

if __name__ == "__main__":
    sol = Solution()
    print(repr(sol.reverseWords("the sky is blue")))
    print(repr(sol.reverseWords("  hello world  ")))
    print(repr(sol.reverseWords("a good   example")))

```
