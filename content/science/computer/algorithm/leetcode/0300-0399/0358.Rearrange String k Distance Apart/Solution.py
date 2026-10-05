from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        cnt = Counter(s)
        pq = [(-v, c) for c, v in cnt.items()]
        heapq.heapify(pq)
        q = deque()
        ans = []
        while pq:
            v, c = heapq.heappop(pq)
            ans.append(c)
            q.append((v + 1, c))
            if len(q) >= k:
                e = q.popleft()
                if e[0]:
                    heapq.heappush(pq, e)
        return "" if len(ans) < len(s) else "".join(ans)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.rearrangeString("aabbcc", 3)) # "abcabc"
    print(sol.rearrangeString("aaabc", 3))  # ""
    print(sol.rearrangeString("aaadbbcc", 2)) # "abacabcd"
