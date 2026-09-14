from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next

# 本地测试辅助函数
def build_list(arr):
    if not arr:
        return None
    cur = head = ListNode(arr[0])
    for v in arr[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def print_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
   print("[" + ",".join(res) + "]")

if __name__ == "__main__":
    sol = Solution()
    h1 = build_list([1,2,3,4,5])
    print_list(sol.removeNthFromEnd(h1, 2))   # [1,2,3,5]

    h2 = build_list([1])
    print_list(sol.removeNthFromEnd(h2, 1))   # []

    h3 = build_list([1,2])
    print_list(sol.removeNthFromEnd(h3, 1))  # [1]
