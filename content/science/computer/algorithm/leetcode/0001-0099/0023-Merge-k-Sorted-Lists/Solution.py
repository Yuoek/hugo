from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, idx, head))
        dummy = cur = ListNode()
        while pq:
            val, idx, node = heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq, (node.next.val, idx, node.next))
            cur.next = node
            cur = cur.next
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
    lists = [build([1,4,5]), build([1,3,4]), build([2,6])]
    show(sol.mergeKLists(lists))   # [1,1,2,3,4,4,5,6]
    show(sol.mergeKLists([]))      # []
    show(sol.mergeKLists([None]))  # []
