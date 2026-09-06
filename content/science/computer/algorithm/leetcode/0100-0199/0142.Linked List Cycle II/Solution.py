from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ans = head
                while ans != slow:
                    ans = ans.next
                    slow = slow.next
                return ans
        return None

if __name__ == "__main__":
    head = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    res = Solution().detectCycle(head)
    print(res.val if res else None)
