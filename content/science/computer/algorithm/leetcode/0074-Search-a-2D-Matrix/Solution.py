class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            mid = (left + right) >> 1
            x, y = divmod(mid, n)
            if matrix[x][y] >= target:
                right = mid
            else:
                left = mid + 1
        return matrix[left // n][left % n] == target

if __name__ == "__main__":
    sol = Solution()
    mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(sol.searchMatrix(mat, 3))   # True
    print(sol.searchMatrix(mat, 13))  # False
