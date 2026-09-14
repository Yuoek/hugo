from typing import List,Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], depth: int) -> None:
            if root is None:
                return
            if len(ans) == depth:
                ans.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        ans = []
        dfs(root, 0)
        return ans

if __name__=="__main__":
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(5)
    root.right.right=TreeNode(4)
    sol=Solution()
    print(sol.rightSideView(root)) # [1,3,4]
