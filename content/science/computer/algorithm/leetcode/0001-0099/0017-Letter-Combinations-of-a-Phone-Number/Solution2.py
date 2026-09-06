from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i: int):
            if i >= len(digits):
                ans.append("".join(t))
                return
            for c in d[int(digits[i]) - 2]:
                t.append(c)
                dfs(i + 1)
                t.pop()

        if not digits:
            return []
        d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        t = []
        l = len(digits)
        dfs(0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))   # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(sol.letterCombinations(""))     # []
    print(sol.letterCombinations("2"))    # ["a","b","c"]
