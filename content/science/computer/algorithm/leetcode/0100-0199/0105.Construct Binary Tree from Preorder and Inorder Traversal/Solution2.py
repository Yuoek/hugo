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
