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
