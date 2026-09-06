---
title: 0145.Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return ans[::-1]

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
```

## Solution

```python

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while root:
            if root.right is None:
                ans.append(root.val)
                root = root.left
            else:
                next_node = root.right
                while next_node.left and next_node.left != root:
                    next_node = next_node.left
                if next_node.left != root:
                    ans.append(root.val)
                    next_node.left = root
                    root = root.right
                else:
                    next_node.left = None
                    root = root.left
        return ans[::-1]

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
```
