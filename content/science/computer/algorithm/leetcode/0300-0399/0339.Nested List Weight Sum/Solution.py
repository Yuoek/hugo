# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       if value is not None:
           self._val = value
           self._list = None
       else:
           self._val = None
           self._list = []

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       return self._val is not None

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """
       if self._list is None:
           self._list = []
       self._val = None
       self._list.append(elem)

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """
       self._val = value
       self._list = None

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       return self._val

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       return self._list


from typing import List
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            depth_sum = 0
            for item in nestedList:
                if item.isInteger():
                    depth_sum += item.getInteger() * depth
                else:
                    depth_sum += dfs(item.getList(), depth + 1)
            return depth_sum

        return dfs(nestedList, 1)


if __name__ == "__main__":
    sol = Solution()
    # 用例1: [1,[4,[6]]]，预期：1*1 +4*2 +6*3 = 27
    n1 = NestedInteger(1)
    n4 = NestedInteger(4)
    n6 = NestedInteger(6)
    inner = NestedInteger()
    inner.add(n6)
    mid = NestedInteger()
    mid.add(n4)
    mid.add(inner)
    case1 = [n1, mid]
    print(sol.depthSum(case1)) # 27

    # 用例2: [[1,1],2,[1,1]]，预期：1*2+1*2 +2*1 +1*2+1*2 =10
    a1 = NestedInteger(1)
    a2 = NestedInteger(1)
    lst1 = NestedInteger()
    lst1.add(a1)
    lst1.add(a2)
    b2 = NestedInteger(2)
    a3 = NestedInteger(1)
    a4 = NestedInteger(1)
    lst2 = NestedInteger()
    lst2.add(a3)
    lst2.add(a4)
    case2 = [lst1, b2, lst2]
    print(sol.depthSum(case2)) #10

    # 用例3: [0]，预期0
    case3 = [NestedInteger(0)]
    print(sol.depthSum(case3)) #0
