from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            l1 = list1.val
            l2 = list2.val
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
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
    l1 = build([1,2,4])
    l2 = build([1,3,4])
    show(sol.mergeTwoLists(l1, l2))   # [1,1,2,3,4,4]
    show(sol.mergeTwoLists(build([]), build([]))) # []
    show(sol.mergeTwoLists(build([]), build([0]))) # [0]
