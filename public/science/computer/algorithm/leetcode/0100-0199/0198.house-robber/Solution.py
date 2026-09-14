from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))
        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))
