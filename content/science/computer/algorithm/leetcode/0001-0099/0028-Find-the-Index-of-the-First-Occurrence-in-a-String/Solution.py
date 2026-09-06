class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))   # 0
    print(sol.strStr("leetcode", "leeto"))  # -1
    print(sol.strStr("abc", "bc"))          # 1
    print(sol.strStr("a", "a"))             # 0
    print(sol.strStr("abc", "abcd"))        # -1
