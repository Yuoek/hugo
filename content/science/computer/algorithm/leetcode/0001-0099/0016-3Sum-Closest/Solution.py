from typing import List
from math import inf

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = inf
        for i, v in enumerate(nums):
            j, k = i + 1, n - 1
            while j < k:
                t = v + nums[j] + nums[k]
                if t == target:
                    return t
                if abs(t - target) < abs(ans - target):
                    ans = t
                if t > target:
                    k -= 1
                else:
                    j += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1,2,1,-4], 1))  # 2
    print(sol.threeSumClosest([0,0,0], 1))       # 0
    print(sol.threeSumClosest([1,1,-1,-1,3], -1)) # -1
