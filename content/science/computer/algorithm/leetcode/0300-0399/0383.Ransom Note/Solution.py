from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(magazine)
        for c in ransomNote:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b"))      # False
    print(sol.canConstruct("aa", "ab"))    # False
    print(sol.canConstruct("aa", "aab"))   # True
