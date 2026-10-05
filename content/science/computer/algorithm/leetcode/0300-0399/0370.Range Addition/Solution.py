from typing import List
from itertools import accumulate

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        d = [0] * length
        for l, r, c in updates:
            d[l] += c
            if r + 1 < length:
                d[r + 1] -= c
        return list(accumulate(d))

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]])) # [-2,0,3,5,3]
