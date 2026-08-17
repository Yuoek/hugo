from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = ListNode()
        r = ListNode()
        tl, tr = l, r
        while head:
            if head.val < x:
                tl.next = head
                tl = tl.next
            else:
                tr.next = head
                tr = tr.next
            head = head.next
        tr.next = None
        tl.next = r.next
        return l.next

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
    print_list(sol.partition(build([1,4,3,2,5,2]), 3)) # [1,2,2,4,3,5]
