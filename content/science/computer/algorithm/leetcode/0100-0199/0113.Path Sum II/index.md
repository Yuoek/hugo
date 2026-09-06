---
title: 0113 路径总和 II
date: 2026-09-03
---

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, s):
            if root is None:
                return
            s += root.val
            t.append(root.val)
            # 叶子节点且总和匹配，拷贝一份存入ans
            if root.left is None and root.right is None and s == targetSum:
                ans.append(t[:])
            dfs(root.left, s)
            dfs(root.right, s)
            t.pop() # 回溯，撤销当前节点

        ans = []
        t = []
        dfs(root, 0)
        return ans


# ----------------本地测试----------------
if __name__ == "__main__":
    #       5
    #     /   \
    #    4     8
    #   /     / \
    #  11    13  4
    # /  \      / \
    #7    2    5   1
    root1 = TreeNode(5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
    )
    print(Solution().pathSum(root1, 22))
    # [[5,4,11,2],[5,8,4,5]]

    print(Solution().pathSum(None, 0)) # []
    print(Solution().pathSum(TreeNode(1), 1)) # [[1]]

    root2 = TreeNode(1, TreeNode(2))
    print(Solution().pathSum(root2, 1)) # [] 根不是叶子
```
