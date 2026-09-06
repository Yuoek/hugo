from collections import deque, defaultdict
from typing import List

class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        def dfs(path, cur):
            if cur == beginWord:
                ans.append(path[::-1])
                return
            for precursor in prev[cur]:
                path.append(precursor)
                dfs(path, precursor)
                path.pop()

        ans = []
        words = set(wordList)
        if endWord not in words:
            return ans
        words.discard(beginWord)
        dist = {beginWord: 0}
        prev = defaultdict(set)
        q = deque([beginWord])
        found = False
        step = 0
        while q and not found:
            step += 1
            level_set = set()
            for _ in range(len(q)):
                p = q.popleft()
                s = list(p)
                for idx in range(len(s)):
                    origin_char = s[idx]
                    for c_ord in range(26):
                        s[idx] = chr(ord('a') + c_ord)
                        t = ''.join(s)
                        if t in dist and dist[t]==step:
                            prev[t].add(p)
                        if t not in words:
                            continue
                        prev[t].add(p)
                        level_set.add(t)
                        dist[t] = step
                        if t == endWord:
                            found = True
                    s[idx] = origin_char
            for w in level_set:
                words.discard(w)
                q.append(w)
        if found:
            path = [endWord]
            dfs(path, endWord)
        return ans

# 本地测试入口
if __name__ == "__main__":
    sol = Solution()
    res = sol.findLadders(
        beginWord="hit",
        endWord="cog",
        wordList=["hot","dot","dog","lot","log","cog"]
    )
    print(res)
