from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = f = g = nums[0]
        for x in nums[1:]:
            ff, gg = f, g
            f = max(x, ff * x, gg * x)
            g = min(x, ff * x, gg * x)
            ans = max(ans, f)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))
    print(sol.maxProduct([-2,0,-1]))
    print(sol.maxProduct([-2,3,-4]))
