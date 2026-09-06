from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum(num >> i & 1 for num in nums)
            if cnt % 3:
                if i == 31:
                    ans -= 1 << i
                else:
                    ans |= 1 << i
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,3,2]))       # 3
    print(sol.singleNumber([0,1,0,1,0,1,99])) # 99
    print(sol.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])) # -4
