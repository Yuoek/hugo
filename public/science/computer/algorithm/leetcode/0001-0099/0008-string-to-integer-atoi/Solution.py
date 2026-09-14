class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        if n == 0:
            return 0
        i = 0
        while s[i] == ' ':
            i += 1
            if i == n:
                return 0
        sign = -1 if s[i] == '-' else 1
        if s[i] in ['-', '+']:
            i += 1
        res, flag = 0, (2**31 - 1) // 10
        while i < n:
            if not s[i].isdigit():
                break
            c = int(s[i])
            if res > flag or (res == flag and c > 7):
                return 2**31 - 1 if sign > 0 else -(2**31)
            res = res * 10 + c
            i += 1
        return sign * res


# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))                 # 42
    print(sol.myAtoi("   -42"))             # -42
    print(sol.myAtoi("4193 with words"))    # 4193
    print(sol.myAtoi("words and 987"))      # 0
    print(sol.myAtoi("-91283472332"))       # -2147483648
    print(sol.myAtoi("2147483648"))         # 2147483647
    print(sol.myAtoi("   "))                # 0
