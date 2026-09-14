from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        ans = 0
        while True:
            ans += 1
            for _ in range(len(q)):
                node = q.popleft()
                # 遇到第一个叶子节点，直接返回当前层数
                if node.left is None and node.right is None:
                    return ans
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


# ----------------本地测试----------------
if __name__ == "__main__":
    #      3
    #    /   \
    #   9    20
    #       /  \
    #      15   7
    root1 = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(Solution().minDepth(root1)) # 2

    # 单边树
    #    1
    #     \
    #      2
    #       \
    #        3
    root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(Solution().minDepth(root2)) # 3

    print(Solution().minDepth(None)) # 0
    print(Solution().minDepth(TreeNode(5))) # 1
