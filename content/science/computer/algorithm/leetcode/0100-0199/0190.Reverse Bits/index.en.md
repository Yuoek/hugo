---
title: 0190.Reverse Bits
date: 2026-09-06
---

## Solution

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= (n & 1) << (31 - i)
            n >>= 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(0b00000010100101000001111010011100)) #964176192
```
