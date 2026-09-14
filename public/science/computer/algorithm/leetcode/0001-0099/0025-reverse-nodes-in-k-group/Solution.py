from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            cur = head
            while cur:
                nxt = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = nxt
            return dummy.next

        dummy = pre = ListNode(next=head)
        while pre:
            cur = pre
            for _ in range(k):
                cur = cur.next
                if cur is None:
                    return dummy.next
            node = pre.next
            nxt = cur.next
            cur.next = None
            pre.next = reverse(node)
            node.next = nxt
            pre = node
        return dummy.next

# 本地测试工具
def build(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    p = head
    for v in arr[1:]:
        p.next = ListNode(v)
        p = p.next
    return head

def show(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(f"[{','.join(res)}]")

if __name__ == "__main__":
    sol = Solution()
    show(sol.reverseKGroup(build([1,2,3,4,5]), 2))  # [2,1,4,3,5]
    show(sol.reverseKGroup(build([1,2,3,4,5]), 3))  # [3,2,1,4,5]
    show(sol.reverseKGroup(build([1]), 1))          # [1]
    show(sol.reverseKGroup(build([]), 2))           # []
