from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, s: int):
            if s == 0:
                ans.append(t[:])
                return
            if i >= len(candidates) or s < candidates[i]:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                t.append(candidates[j])
                dfs(j + 1, s - candidates[j])
                t.pop()

        candidates.sort()
        ans = []
        t = []
        dfs(0, target)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
    # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(sol.combinationSum2([2,5,2,1,2], 5))
    # [[1,2,2],[5]]
