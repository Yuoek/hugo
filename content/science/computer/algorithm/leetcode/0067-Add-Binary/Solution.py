class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or carry:
            carry += (0 if i < 0 else int(a[i])) + (0 if j < 0 else int(b[j]))
            carry, v = divmod(carry, 2)
            ans.append(str(v))
            i, j = i - 1, j - 1
        return "".join(ans[::-1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))      # "100"
    print(sol.addBinary("1010", "1011"))  # "10101"
    print(sol.addBinary("0", "0"))        # "0"
