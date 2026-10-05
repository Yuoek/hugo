---
title: 0359 日志速率限制器
date: 2026-09-18
---

## Solution

```python
class Logger:

    def __init__(self):
        self.ts = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        t = self.ts.get(message, 0)
        if t > timestamp:
            return False
        self.ts[message] = timestamp + 10
        return True

# 本地测试
if __name__ == "__main__":
    obj = Logger()
    print(obj.shouldPrintMessage(1, "foo"))  # True
    print(obj.shouldPrintMessage(2, "bar"))  # True
    print(obj.shouldPrintMessage(3, "foo"))  # False
    print(obj.shouldPrintMessage(8, "bar"))  # False
    print(obj.shouldPrintMessage(10, "foo")) # False
    print(obj.shouldPrintMessage(11, "foo")) # True
```
