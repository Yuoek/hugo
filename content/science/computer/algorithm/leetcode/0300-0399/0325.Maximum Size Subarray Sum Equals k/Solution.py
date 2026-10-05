from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {0: -1}
        ans = s = 0
        for i, x in enumerate(nums):
            s += x
            if s - k in d:
                ans = max(ans, i - d[s - k])
            if s not in d:
                d[s] = i
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArrayLen([1, -1, 5, -2, 3], 3))  # 4
    print(sol.maxSubArrayLen([-2, -1, 2, 1], 1))     # 2
