from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            x = numbers[i] + numbers[j]
            if x == target:
                return [i + 1, j + 1]
            if x < target:
                i += 1
            else:
                j -= 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([2,3,4],6))
    print(sol.twoSum([-1,0],-1))
