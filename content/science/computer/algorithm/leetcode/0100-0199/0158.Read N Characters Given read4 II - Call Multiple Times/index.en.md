---
title: 0158.Read N Characters Given read4 II - Call Multiple Times
date: 2026-09-05
---

## Solution

```python
from typing import List

# 模拟底层API
def read4(buf4: List[str]) -> int:
    global fp
    text = "abcdefghijklmnopqrstuvwxyz"
    cnt = 0
    while fp < len(text) and cnt < 4:
        buf4[cnt] = text[fp]
        fp += 1
        cnt += 1
    return cnt

class Solution:
    def __init__(self):
        self.buf4 = [None] * 4
        self.i = self.size = 0

    def read(self, buf: List[str], n: int) -> int:
        j = 0
        while j < n:
            if self.i == self.size:
                self.size = read4(self.buf4)
                self.i = 0
                if self.size == 0:
                    break
            while j < n and self.i < self.size:
                buf[j] = self.buf4[self.i]
                self.i += 1
                j += 1
        return j

if __name__ == "__main__":
    global fp
    fp = 0
    sol = Solution()
    buf = [""] * 5
    print(sol.read(buf,5), buf[:5])
    print(sol.read(buf,5), buf[:5])
```
