from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque([beginWord])
        ans = 1
        while q:
            ans += 1
            for _ in range(len(q)):
                s = q.popleft()
                s_list = list(s)
                for i in range(len(s_list)):
                    origin = s_list[i]
                    for j in range(26):
                        s_list[i] = chr(ord('a') + j)
                        t = ''.join(s_list)
                        if t not in words:
                            continue
                        if t == endWord:
                            return ans
                        q.append(t)
                        words.remove(t)
                    s_list[i] = origin
        return 0

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    # 预期输出：5
