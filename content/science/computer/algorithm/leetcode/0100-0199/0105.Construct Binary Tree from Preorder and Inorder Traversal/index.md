---
title: 0105 从前序与中序遍历序列构造二叉树
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
```

## Solution 2

```python
from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getBinaryTrees(self, preOrder: List[int], inOrder: List[int]) -> List[Optional[TreeNode]]:
        def dfs(i: int, j: int, n: int) -> List[Optional[TreeNode]]:
            if n <= 0:
                return [None]
            v = preOrder[i]
            ans = []
            # k 是根在 inOrder 里的下标，同一个值可以出现在多处
            for k in d[v]:
                # k 必须落在当前 inorder 片段 [j, j+n‑1] 区间内
                if j <= k < j + n:
                    left_list = dfs(i + 1, j, k - j)
                    right_list = dfs(i + 1 + k - j, k + 1, n - 1 - (k - j))
                    for l in left_list:
                        for r in right_list:
                            ans.append(TreeNode(v, l, r))
            return ans

        d = defaultdict(list)
        for idx, val in enumerate(inOrder):
            d[val].append(idx)
        return dfs(0, 0, len(preOrder))


# ----------------本地测试----------------
if __name__ == "__main__":
    # 工具：前序遍历打印树
    def pre_show(node):
        if not node:
            return []
        return [node.val] + pre_show(node.left) + pre_show(node.right)

    # 示例：值重复，有多棵合法树
    pre = [1,1]
    inn = [1,1]
    trees = Solution().getBinaryTrees(pre, inn)
    print(f"一共 {len(trees)} 棵树")
    for t in trees:
        print(pre_show(t))
    '''
    2棵树
    [1, 1]
    [1, 1]
    结构：
    ① root=1 left=1 right=None
    ② root=1 left=None right=1
    '''
```
