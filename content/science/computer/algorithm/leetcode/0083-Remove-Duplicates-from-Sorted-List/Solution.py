from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

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
    print_list(sol.deleteDuplicates(build([1,1,2])))         # [1,2]
    print_list(sol.deleteDuplicates(build([1,1,2,3,3])))     # [1,2,3]
