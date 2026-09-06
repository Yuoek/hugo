from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        d = defaultdict(int)
        for x in nums:
            y = x
            while y in s:
                s.remove(y)
                y += 1
            d[x] = d[y] + y - x
            ans = max(ans, d[x])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2])) # 预期4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #预期9
    print(sol.longestConsecutive([])) #0
