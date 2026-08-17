from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1
        i, j = m - 1, n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

if __name__ == "__main__":
    sol = Solution()
    a = [1,2,3,0,0,0]
    sol.merge(a,3,[2,5,6],3)
    print(a) # [1, 2, 2, 3, 5, 6]
