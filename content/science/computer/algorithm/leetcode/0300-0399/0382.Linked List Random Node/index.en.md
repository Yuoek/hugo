---
title: 0382.Linked List Random Node
date: 2026-09-18
---

## Solution

```python
import random
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        n = ans = 0
        head = self.head
        while head:
            n += 1
            x = random.randint(1, n)
            if n == x:
                ans = head.val
            head = head.next
        return ans

# 本地测试
if __name__ == "__main__":
    def build(arr):
        if not arr:
            return None
        h = ListNode(arr[0])
        cur = h
        for v in arr[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return h
    sol = Solution(build([1,2,3]))
    print([sol.getRandom() for _ in range(10)])
```
