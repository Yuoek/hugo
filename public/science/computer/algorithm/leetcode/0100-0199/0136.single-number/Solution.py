from functools import reduce
from operator import xor
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,1]))   # 1
    print(sol.singleNumber([4,1,2,1,2])) # 4
    print(sol.singleNumber([1])) # 1
