from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(5)) # [0,1,1,2,1,2]
