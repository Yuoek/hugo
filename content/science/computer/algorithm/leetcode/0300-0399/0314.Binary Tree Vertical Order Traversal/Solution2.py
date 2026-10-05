from typing import List, Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root, 0)])
        d = defaultdict(list)
        while q:
            for _ in range(len(q)):
                node, offset = q.popleft()
                d[offset].append(node.val)
                if node.left:
                    q.append((node.left, offset - 1))
                if node.right:
                    q.append((node.right, offset + 1))
        return [v for _, v in sorted(d.items())]

def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(2)
    root.right.left.left = TreeNode(5)
    sol = Solution()
    print(sol.verticalOrder(root))

if __name__ == "__main__":
    main()
