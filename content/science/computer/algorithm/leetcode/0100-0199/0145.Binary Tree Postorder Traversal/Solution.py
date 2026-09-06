from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)

        ans = []
        dfs(root)
        return ans

if __name__ == "__main__":
    #     1
    #      \
    #       2
    #      /
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    sol = Solution()
    print(sol.postorderTraversal(root))
