---
title: 0394 字符串解码
date: 2026-09-18
---

## Solution

```python
class Solution:
    def decodeString(self, s: str) -> str:
        s1, s2 = [], []
        num, res = 0, ''
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                s1.append(num)   # 存放倍数
                s2.append(res)   # 存放[前面的字符串
                num, res = 0, ''
            elif c == ']':
                # 弹出倍数，当前res重复倍数次，拼接到之前保存的字符串
                res = s2.pop() + res * s1.pop()
            else:
                res += c
        return res

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))      # aaabcbc
    print(sol.decodeString("3[a2[c]]"))       # accaccacc
    print(sol.decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
```
