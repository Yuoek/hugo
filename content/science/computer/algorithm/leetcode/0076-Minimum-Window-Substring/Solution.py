from collections import Counter
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        cnt = l = 0
        k, mi = -1, inf
        for r, c in enumerate(s):
            window[c] += 1
            if need[c] >= window[c]:
                cnt += 1
            while cnt == len(t):
                if r - l + 1 < mi:
                    mi = r - l + 1
                    k = l
                if need[s[l]] >= window[s[l]]:
                    cnt -= 1
                window[s[l]] -= 1
                l += 1
        return "" if k < 0 else s[k : k + mi]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC")) # BANC
    print(sol.minWindow("a", "a"))               # a
    print(sol.minWindow("a", "aa"))              # ""
