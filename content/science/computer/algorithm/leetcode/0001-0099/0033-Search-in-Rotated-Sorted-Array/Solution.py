from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid
        return left if nums[left] == target else -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))   # 4
    print(sol.search([4,5,6,7,0,1,2], 3))   # -1
    print(sol.search([1], 0))                # -1
    print(sol.search([1,3], 3))              # 1
    print(sol.search([3,1], 1))              # 1
