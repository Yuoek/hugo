---
title: 0144.Binary Tree Preorder Traversal
date: 2026-09-05
---

## Solution

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root is None:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

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
    print(sol.preorderTraversal(root))
```

## Solution 2

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
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
    print(sol.preorderTraversal(root))
```

## Solution 3

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while root:
            if root.left is None:
                ans.append(root.val)
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if prev.right is None:
                    ans.append(root.val)
                    prev.right = root
                    root = root.left
                else:
                    prev.right = None
                    root = root.right
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
    print(sol.preorderTraversal(root))
```
