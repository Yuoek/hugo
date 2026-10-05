from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        x = 0
        mx = (1 << 31) - 1
        for _ in range(n):
            x = heapq.heappop(q)
            for k in primes:
                if x <= mx // k:
                    heapq.heappush(q, k * x)
                if x % k == 0:
                    break
        return x


if __name__ == "__main__":
    sol = Solution()
    print(sol.nthSuperUglyNumber(12, [2,7,13,19])) #32
    print(sol.nthSuperUglyNumber(1, [2,3,5])) #1
