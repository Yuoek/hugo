---
title: 0141.Linked List Cycle
date: 2026-09-05
---

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

if __name__ == "__main__":
    # 有环样例
    head = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    head.next = b
    b.next = c
    c.next = d
    d.next = b
    print(Solution().hasCycle(head))
```

## Solution 2

```python
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    head = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    print(Solution().hasCycle(head))
```
