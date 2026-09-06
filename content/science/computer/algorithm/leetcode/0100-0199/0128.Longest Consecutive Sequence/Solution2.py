from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for x in s:
            # x-1不在集合，说明x是一段连续序列的起点
            if x - 1 not in s:
                y = x + 1
                while y in s:
                    y += 1
                ans = max(ans, y - x)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))    # 4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
    print(sol.longestConsecutive([]))                    # 0
    print(sol.longestConsecutive([1,2,0,1]))              # 3
