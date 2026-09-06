from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
# 测试1：相同树
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(Solution().isSameTree(p1, q1)) # True

# 测试2：结构不同
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    print(Solution().isSameTree(p2, q2)) # False

# 测试3：一棵空，一棵非空
    p3 = None
    q3 = TreeNode(0)
    print(Solution().isSameTree(p3, q3)) # False

# 测试4：两棵都空
    p4 = None
    q4 = None
    print(Solution().isSameTree(p4, q4)) # True
