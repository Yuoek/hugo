---
title: 0393 UTF-8 编码验证
date: 2026-09-18
---

## Solution

```python
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0
        for v in data:
            if cnt > 0:
                # 后续字节必须以 10 开头
                if v >> 6 != 0b10:
                    return False
                cnt -= 1
            elif v >> 7 == 0:
                # 1字节字符：0xxxxxxx
                cnt = 0
            elif v >> 5 == 0b110:
                # 2字节：110xxxxx
                cnt = 1
            elif v >> 4 == 0b1110:
                # 3字节：1110xxxx
                cnt = 2
            elif v >> 3 == 0b11110:
                # 4字节：11110xxx
                cnt = 3
            else:
                # 非法开头 11111xxx 或者 10xxxxxx作为起始
                return False
        return cnt == 0

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.validUtf8([197,130,1]))    # True
    print(sol.validUtf8([235,140,4]))    # False
    print(sol.validUtf8([250,145,145,145,145])) #True
```
