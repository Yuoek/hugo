from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        f = g = 0
        for x in nums:
            f, g = max(f, g), f + x
        return max(f, g)

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))
