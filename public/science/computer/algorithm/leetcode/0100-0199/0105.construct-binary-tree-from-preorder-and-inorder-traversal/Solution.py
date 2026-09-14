from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(i: int, j: int, n: int) -> Optional[TreeNode]:
            if n <= 0:
                return None
            v = preorder[i]
            k = d[v]
            l = dfs(i + 1, j, k - j)
            r = dfs(i + 1 + k - j, k + 1, n - (k - j) - 1)
            return TreeNode(v, l, r)

        d = {v: idx for idx, v in enumerate(inorder)}
        return dfs(0, 0, len(preorder))


# ----------------本地测试----------------
if __name__ == "__main__":
    # preorder = [3,9,20,15,7]
    # inorder  = [9,3,15,20,7]
    pre = [3,9,20,15,7]
    inn = [9,3,15,20,7]
    root = Solution().buildTree(pre, inn)

    # 简单打印验证结构
    def show(node):
        if not node:
            return
        print(node.val, end=" ")
        show(node.left)
        show(node.right)
    show(root) # 3 9 20 15 7
