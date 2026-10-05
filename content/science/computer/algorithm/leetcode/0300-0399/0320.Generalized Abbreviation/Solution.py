from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(i: int) -> List[str]:
            if i >= n:
                return [""]
            # 不缩写当前字符，直接保留word[i]
            ans = [word[i] + s for s in dfs(i + 1)]
            # 从i开始，缩写长度 j-i 的字符
            for j in range(i + 1, n + 1):
                for s in dfs(j + 1):
                    suffix = word[j] if j < n else ""
                    ans.append(str(j - i) + suffix + s)
            return ans

        n = len(word)
        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateAbbreviations("word"))
