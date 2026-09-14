from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(v) for v in nums]
        nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        return "0" if nums[0] == "0" else "".join(nums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([10,2]))
    print(sol.largestNumber([3,30,34,5,9]))
    print(sol.largestNumber([0,0]))
