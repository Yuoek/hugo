---
title: 0061 旋转链表
date: 2026-08-16
weight: 61
summary: lc
---

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur, n = head, 0
        while cur:
            n += 1
            cur = cur.next
        k %= n
        if k == 0:
            return head
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next

        ans = slow.next
        slow.next = None
        fast.next = head
        return ans

# 本地测试辅助
def build(arr):
    dummy = ListNode()
    p = dummy
    for v in arr:
        p.next = ListNode(v)
        p = p.next
    return dummy.next

def show(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print("->".join(res))

if __name__ == "__main__":
    sol = Solution()
    h = build([1,2,3,4,5])
    nh = sol.rotateRight(h, 2)
    show(nh)

```
