class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

if __name__ == "__main__":
    sol = Solution()
    print(repr(sol.reverseWords("the sky is blue")))
    print(repr(sol.reverseWords("  hello world  ")))
    print(repr(sol.reverseWords("a good   example")))
