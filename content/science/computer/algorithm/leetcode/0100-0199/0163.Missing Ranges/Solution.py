from typing import List
from itertools import pairwise

class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[lower, upper]]
        ans = []
        if nums[0] > lower:
            ans.append([lower, nums[0] - 1])
        for a, b in pairwise(nums):
            if b - a > 1:
                ans.append([a + 1, b - 1])
        if nums[-1] < upper:
            ans.append([nums[-1] + 1, upper])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMissingRanges([0,1,3,50,75],0,99))
    print(sol.findMissingRanges([],1,1))
