from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for c in nums:
            aa = (~a & b & c) | (a & ~b & ~c)
            bb = ~a & (b ^ c)
            a, b = aa, bb
        return b


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,3,2]))                 # 3
    print(sol.singleNumber([0,1,0,1,0,1,99]))          # 99
    print(sol.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])) # -4
