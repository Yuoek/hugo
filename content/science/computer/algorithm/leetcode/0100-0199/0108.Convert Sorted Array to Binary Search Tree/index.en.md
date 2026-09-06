---
title: 0108.Convert Sorted Array to Binary Search Tree
date: 2026-09-03
---

## Solution

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) >> 1
            return TreeNode(nums[mid], dfs(l, mid - 1), dfs(mid + 1, r))

        return dfs(0, len(nums) - 1)


# ----------------本地测试----------------
if __name__ == "__main__":
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    nums1 = [-10,-3,0,5,9]
    root1 = Solution().sortedArrayToBST(nums1)
    print(inorder(root1)) # [-10, -3, 0, 5, 9]

    print(Solution().sortedArrayToBST([])) # None
    print(inorder(Solution().sortedArrayToBST([1]))) # [1]
```
