---
title: 0379 电话目录管理系统
date: 2026-09-18
---

## Solution

```python
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        if not self.available:
            return -1
        return self.available.pop()

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        self.available.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

# 本地测试
if __name__ == "__main__":
    obj = PhoneDirectory(3)
    print(obj.get())      # 随机0/1/2
    print(obj.check(2))
    print(obj.get())
    print(obj.get())
    print(obj.get())      # -1
    obj.release(2)
    print(obj.check(2))   # True
    print(obj.get())      # 2
```
