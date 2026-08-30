---
title: 0092 反转链表 II
date: 2026-08-17
weight: 92
summary: 链表
---

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        p, q = pre, pre.next
        cur = q
        for _ in range(right - left + 1):
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        p.next = pre
        q.next = cur
        return dummy.next

# 测试辅助
def build(arr):
    if not arr: return None
    h = ListNode(arr[0])
    p = h
    for v in arr[1:]:
        p.next = ListNode(v)
        p = p.next
    return h

def print_list(h):
    res = []
    while h:
        res.append(h.val)
        h = h.next
    print(res)

if __name__ == "__main__":
    sol = Solution()
    print_list(sol.reverseBetween(build([1,2,3,4,5]), 2, 4))
    # [1,4,3,2,5]

```
