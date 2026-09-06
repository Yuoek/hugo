from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            if i == n:
                ans.append(t[:])
                return
            for j in range(n):
                if vis[j] or (j and nums[j] == nums[j - 1] and not vis[j - 1]):
                    continue
                t[i] = nums[j]
                vis[j] = True
                dfs(i + 1)
                vis[j] = False

        n = len(nums)
        nums.sort()
        ans = []
        t = [0] * n
        vis = [False] * n
        dfs(0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([1,1,2]))
    # [[1,1,2],[1,2,1],[2,1,1]]
    print(sol.permuteUnique([1,2,3]))
    print(sol.permuteUnique([2,2,1,1]))
