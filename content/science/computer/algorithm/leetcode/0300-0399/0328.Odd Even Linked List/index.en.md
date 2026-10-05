---
title: 0328.Odd Even Linked List
date: 2026-09-17
---

## Solution

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        a = head
        b = c = head.next
        while b and b.next:
            a.next = b.next
            a = a.next
            b.next = a.next
            b = b.next
        a.next = c
        return head

if __name__ == "__main__":
    # 辅助打印链表
    def print_list(head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

    # 构造链表 1->2->3->4->5
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    sol = Solution()
    print_list(sol.oddEvenList(n1)) # [1,3,5,2,4]

    # 构造链表 2->1->3->5->6->4->7
    m1 = ListNode(2)
    m2 = ListNode(1)
    m3 = ListNode(3)
    m4 = ListNode(5)
    m5 = ListNode(6)
    m6 = ListNode(4)
    m7 = ListNode(7)
    m1.next=m2;m2.next=m3;m3.next=m4;m4.next=m5;m5.next=m6;m6.next=m7
    print_list(sol.oddEvenList(m1)) # [2,3,6,7,1,5,4]

```
