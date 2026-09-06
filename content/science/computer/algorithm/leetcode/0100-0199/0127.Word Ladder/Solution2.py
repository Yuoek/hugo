from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def extend(m1, m2, q):
            for _ in range(len(q)):
                s = q.popleft()
                step = m1[s]
                s_list = list(s)
                for i in range(len(s_list)):
                    origin = s_list[i]
                    for j in range(26):
                        s_list[i] = chr(ord('a') + j)
                        t = ''.join(s_list)
                        if t in m1 or t not in words:
                            continue
                        if t in m2:
                            return step + 1 + m2[t]
                        m1[t] = step + 1
                        q.append(t)
                    s_list[i] = origin
            return -1

        words = set(wordList)
        if endWord not in words:
            return 0
        q1, q2 = deque([beginWord]), deque([endWord])
        m1, m2 = {beginWord: 0}, {endWord: 0}
        while q1 and q2:
            # 选择更小队列扩展，优化性能
            if len(q1) <= len(q2):
                res = extend(m1, m2, q1)
            else:
                res = extend(m2, m1, q2)
            if res != -1:
                return res + 1
        return 0

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    # 输出 5
