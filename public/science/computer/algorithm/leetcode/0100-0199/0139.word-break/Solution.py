from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        f = [True] + [False] * n
        for i in range(1, n + 1):
            f[i] = any(f[j] and s[j:i] in words for j in range(i))
        return f[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet","code"]))          # True
    print(sol.wordBreak("applepenapple", ["apple","pen"]))     # True
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # False
