from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        target = dummy
        while head:
            if head.val != 9:
                target = head
            head = head.next
        target.val += 1
        target = target.next
        while target:
            target.val = 0
            target = target.next
        return dummy if dummy.val else dummy.next

# 本地测试
if __name__ == "__main__":
    def build(arr):
        if not arr:
            return None
        h = ListNode(arr[0])
        cur = h
        for v in arr[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return h
    def printList(node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        print(res)

    sol = Solution()
    printList(sol.plusOne(build([1,2,3]))) # [1,2,4]
    printList(sol.plusOne(build([9,9,9]))) # [1,0,0,0]
    printList(sol.plusOne(build([4,9,9]))) # [5,0,0]
