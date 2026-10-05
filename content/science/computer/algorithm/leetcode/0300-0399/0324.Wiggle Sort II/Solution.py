from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        n = len(arr)
        i, j = (n - 1) >> 1, n - 1
        for k in range(n):
            if k % 2 == 0:
                nums[k] = arr[i]
                i -= 1
            else:
                nums[k] = arr[j]
                j -= 1

if __name__ == "__main__":
    sol = Solution()
    test1 = [1,5,1,1,6,4]
    sol.wiggleSort(test1)
    print(test1) # [1,6,1,5,1,4]
    test2 = [1,3,2,2,3,1]
    sol.wiggleSort(test2)
    print(test2) # [2,3,1,3,1,2]
