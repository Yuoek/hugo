---
title: 0082 删除链表中的重复元素 II
date: 2026-08-17
weight: 82
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(next=head)
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
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
    print_list(sol.deleteDuplicates(build([1,2,3,3,4,4,5]))) # [1,2,5]
    print_list(sol.deleteDuplicates(build([1,1,1,2,3])))    # [2,3]

```
