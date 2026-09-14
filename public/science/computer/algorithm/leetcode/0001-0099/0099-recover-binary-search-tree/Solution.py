from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if root is None:
                return
            nonlocal prev, first, second
            dfs(root.left)
            if prev and prev.val > root.val:
                if first is None:
                    first = prev
                second = root
            prev = root
            dfs(root.right)

        prev = first = second = None
        dfs(root)
        first.val, second.val = second.val, first.val

# 测试辅助
def inorder(root):
    res = []
    def d(x):
        if not x: return
        d(x.left)
        res.append(x.val)
        d(x.right)
    d(root)
    return res

if __name__ == "__main__":
    # 输入 [3,1,4,null,null,2]
    r = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    sol = Solution()
    sol.recoverTree(r)
    print(inorder(r)) # [1,2,3,4]
