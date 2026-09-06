class Solution:
    def intToRoman(self, num: int) -> str:
        cs = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        vs = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        ans = []
        for c, v in zip(cs, vs):
            while num >= v:
                num -= v
                ans.append(c)
        return ''.join(ans)


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3))      # III
    print(sol.intToRoman(58))     # LVIII
    print(sol.intToRoman(1994))   # MCMXCIV
