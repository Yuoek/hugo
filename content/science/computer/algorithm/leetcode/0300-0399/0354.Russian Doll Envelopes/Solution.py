import bisect
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        d = [envelopes[0][1]]
        for _, h in envelopes[1:]:
            if h > d[-1]:
                d.append(h)
            else:
                idx = bisect.bisect_left(d, h)
                d[idx] = h
        return len(d)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])) # 3
    print(sol.maxEnvelopes([[1,1],[1,1],[1,1]])) # 1
