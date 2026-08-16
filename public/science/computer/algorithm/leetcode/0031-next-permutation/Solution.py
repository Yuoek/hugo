from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = next((i for i in range(n - 2, -1, -1) if nums[i] < nums[i + 1]), -1)
        isi = ~i
        if ~i:
            j = next((j for j in range(n - 1, i, -1) if nums[j] > nums[i]))
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = nums[i + 1 :][::-1]

if __name__ == "__main__":
    sol = Solution()
    arr1 = [1,2,3]
    sol.nextPermutation(arr1)
    print(arr1)     # [1,3,2]

    arr2 = [3,2,1]
    sol.nextPermutation(arr2)
    print(arr2)     # [1,2,3]

    arr3 = [1,1,5]
    sol.nextPermutation(arr3)
    print(arr3)     # [1,5,1]

    arr4 = [1,3,2]
    sol.nextPermutation(arr4)
    print(arr4)     # [2,1,3]
