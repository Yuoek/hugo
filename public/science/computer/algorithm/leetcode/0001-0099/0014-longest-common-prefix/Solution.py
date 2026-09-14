from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if len(s) <= i or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))  # fl
    print(sol.longestCommonPrefix(["dog","racecar","car"]))     # ""
    print(sol.longestCommonPrefix(["apple","app"]))             # app
    print(sol.longestCommonPrefix(["a"]))                       # a
