from typing import Optional, List

# Definition for singly‑linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def dfs(i: int, j: int) -> Optional[TreeNode]:
            if i > j:
                return None
            mid = (i + j) >> 1
            l = dfs(i, mid - 1)
            r = dfs(mid + 1, j)
            return TreeNode(nums[mid], l, r)

        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return dfs(0, len(nums) - 1)


# ----------------本地测试----------------
if __name__ == "__main__":
    # 构建链表 -10 → -3 → 0 →5 →9
    def build_link(arr):
        dummy = ListNode()
        p = dummy
        for v in arr:
            p.next = ListNode(v)
            p = p.next
        return dummy.next

    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    head = build_link([-10,-3,0,5,9])
    root = Solution().sortedListToBST(head)
    print(inorder(root)) # [-10, -3, 0, 5, 9]

    print(Solution().sortedListToBST(None)) # None
    print(inorder(Solution().sortedListToBST(build_link([1])))) # [1]
