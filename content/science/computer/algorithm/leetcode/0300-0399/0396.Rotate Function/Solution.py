from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = sum(i * v for i, v in enumerate(nums))
        n, s = len(nums), sum(nums)
        ans = f
        for i in range(1, n):
            f = f + s - n * nums[n - i]
            ans = max(ans, f)
        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxRotateFunction([4,3,2,6])) # 26
    print(sol.maxRotateFunction([100]))     # 0
