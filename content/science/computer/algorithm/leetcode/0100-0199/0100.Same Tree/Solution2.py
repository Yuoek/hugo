from typing import Optional
from collections import deque

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
        if p is None or q is None:
            return False
        q1, q2 = deque([p]), deque([q])
        while q1 and q2:
            a, b = q1.popleft(), q2.popleft()
            aval = a.val
            bval = b.val
            if a.val != b.val:
                return False
            la, ra = a.left, a.right
            lb, rb = b.left, b.right
            # 左子节点结构不一致：一个有，一个无
            if (la and not lb) or (lb and not la):
                return False
            # 右子节点结构不一致
            if (ra and not rb) or (rb and not ra):
                return False
            if la:
                q1.append(la)
                q2.append(lb)
            if ra:
                q1.append(ra)
                q2.append(rb)
        return True

if __name__ == "__main__":
# 测试1 相同
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(Solution().isSameTree(p1, q1)) # True

# 测试2 结构不同
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    print(Solution().isSameTree(p2, q2)) # False

# 测试3 值不同
    p3 = TreeNode(1, TreeNode(2), TreeNode(3))
    q3 = TreeNode(1, TreeNode(99), TreeNode(3))
    print(Solution().isSameTree(p3, q3)) # False

# 测试4 两棵空
    p4 = None
    q4 = None
    print(Solution().isSameTree(p4, q4)) # True

# 测试5 一空一有
    p5 = None
    q5 = TreeNode(5)
    print(Solution().isSameTree(p5, q5)) # False
