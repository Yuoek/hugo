from typing import List
from collections import defaultdict

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = defaultdict(int)
        ans = 0
        for s in words:
            a = len(s)
            x = 0
            for c in s:
                x |= 1 << (ord(c) - ord("a"))
            for y, b in mask.items():
                if (x & y) == 0:
                    ans = max(ans, a * b)
            mask[x] = max(mask[x], a)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))  # 16
    print(sol.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))      # 4
    print(sol.maxProduct(["a","aa","aaa","aaaa"]))                      # 0
