# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        if value is not None:
            self._val = value
            self._list = None
        else:
            self._val = None
            self._list = []

    def isInteger(self) -> bool:
        return self._val is not None

    def getInteger(self) -> int:
        return self._val

    def getList(self):
        return self._list

    def add(self, elem):
        if self._list is None:
            self._list = []
        self._val = None
        self._list.append(elem)


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def dfs(ls):
            for x in ls:
                if x.isInteger():
                    self.nums.append(x.getInteger())
                else:
                    dfs(x.getList())

        self.nums = []
        self.i = -1
        dfs(nestedList)

    def next(self) -> int:
        self.i += 1
        return self.nums[self.i]

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.nums)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    # 构造样例 [1,[4,[6]]]
    n1 = NestedInteger(1)
    n4 = NestedInteger(4)
    n6 = NestedInteger(6)
    inner = NestedInteger()
    inner.add(n6)
    mid = NestedInteger()
    mid.add(n4)
    mid.add(inner)
    nestedList = [n1, mid]

    it = NestedIterator(nestedList)
    res = []
    while it.hasNext():
        res.append(it.next())
    print(res) # [1,4,6]

    # 构造样例 [[1,1],2,[1,1]]
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
    nestedList2 = [lst1, b2, lst2]
    it2 = NestedIterator(nestedList2)
    res2 = []
    while it2.hasNext():
        res2.append(it2.next())
    print(res2) # [1,1,2,1,1]
