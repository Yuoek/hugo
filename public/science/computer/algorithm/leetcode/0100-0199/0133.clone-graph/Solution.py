from collections import defaultdict
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        def dfs(node):
            if node is None:
                return None
            if node in g:
                return g[node]
            cloned = Node(node.val)
            g[node] = cloned
            for nxt in node.neighbors:
                cloned.neighbors.append(dfs(nxt))
            return cloned

        g = defaultdict()
        return dfs(node)


# 本地测试
if __name__ == "__main__":
    # 构造图：
    # 1 <--> 2
    # 2 <--> 1,3
    # 3 <--> 2,4
    # 4 <--> 3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n3]

    sol = Solution()
    copy = sol.cloneGraph(n1)
    print(copy.val)          # 1
    print(copy.neighbors[0].val) # 2
    print(copy is n1) # False，是全新对象
