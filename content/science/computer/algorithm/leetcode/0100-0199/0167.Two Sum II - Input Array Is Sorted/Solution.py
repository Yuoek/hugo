from typing import List
import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            x = target - numbers[i]
            j = bisect.bisect_left(numbers, x, lo=i + 1)
            if j < n and numbers[j] == x:
                return [i + 1, j + 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([2,3,4],6))
