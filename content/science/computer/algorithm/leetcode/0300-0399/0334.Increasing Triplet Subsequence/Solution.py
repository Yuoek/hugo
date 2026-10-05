from typing import List
from math import inf

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mi, mid = inf, inf
        for num in nums:
            if num > mid:
                return True
            if num <= mi:
                mi = num
            else:
                mid = num
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.increasingTriplet([1,2,3,4,5]))   # True
    print(sol.increasingTriplet([5,4,3,2,1]))   # False
    print(sol.increasingTriplet([2,1,5,0,6]))   # True
    print(sol.increasingTriplet([1,1,1,1]))     # False
