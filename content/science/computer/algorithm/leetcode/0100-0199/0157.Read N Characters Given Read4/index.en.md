---
title: 0157.Read N Characters Given Read4
date: 2026-09-05
---

## Solution

```python
def read4(buf4):
    global file_ptr
    content = "abcdefghijk"
    cnt = 0
    while file_ptr < len(content) and cnt < 4:
        buf4[cnt] = content[file_ptr]
        file_ptr += 1
        cnt += 1
    return cnt

class Solution:
    def read(self, buf, n):
        i = 0
        buf4 = [''] * 4
        while True:
            v = read4(buf4)
            for j in range(v):
                if i >= n:
                    return i
                buf[i] = buf4[j]
                i += 1
            if v < 4:
                break
        return i

if __name__ == "__main__":
    global file_ptr
    file_ptr = 0
    buf = [''] * 8
    sol = Solution()
    length = sol.read(buf,8)
    print(buf[:length])
```
