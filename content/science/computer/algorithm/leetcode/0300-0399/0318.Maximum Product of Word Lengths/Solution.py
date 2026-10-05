from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [0] * len(words)
        ans = 0
        for i, s in enumerate(words):
            for c in s:
                mask[i] |= 1 << (ord(c) - ord("a"))
            for j, t in enumerate(words[:i]):
                if (mask[i] & mask[j]) == 0:
                    ans = max(ans, len(s) * len(t))
        return ans

if __name__ == "__main__":
    sol = Solution()
    # test case1
    words1 = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print(sol.maxProduct(words1)) # expect 16
    # test case2
    words2 = ["a","ab","abc","d","cd","bcd","abcd"]
    print(sol.maxProduct(words2)) # expect 4
    # test case3
    words3 = ["a","aa","aaa","aaaa"]
    print(sol.maxProduct(words3)) # expect 0
