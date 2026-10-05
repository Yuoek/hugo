class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sum(ord(c) for c in s)
        b = sum(ord(c) for c in t)
        return chr(b - a)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde")) # e
    print(sol.findTheDifference("", "y")) # y
