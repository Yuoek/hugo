from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        t = self.swapPairs(head.next.next)
        p = head.next
        p.next = head
        head.next = t
        return p

# 本地测试工具
def build(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for v in arr[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def show(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(f"[{','.join(res)}]")

if __name__ == "__main__":
    sol = Solution()
    show(sol.swapPairs(build([1,2,3,4])))   # [2,1,4,3]
    show(sol.swapPairs(build([])))          # []
    show(sol.swapPairs(build([1])))         # [1]
    show(sol.swapPairs(build([1,2,3])))     # [2,1,3]
