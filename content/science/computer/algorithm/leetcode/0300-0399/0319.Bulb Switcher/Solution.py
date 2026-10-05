from math import sqrt

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))

if __name__ == "__main__":
    sol = Solution()
    print(sol.bulbSwitch(3))   # 1
    print(sol.bulbSwitch(0))   # 0
    print(sol.bulbSwitch(99))  # 9
    print(sol.bulbSwitch(100)) # 10
