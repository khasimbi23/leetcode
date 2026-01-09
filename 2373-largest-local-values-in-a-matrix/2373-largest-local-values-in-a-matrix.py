class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        max_val = max(max_val, grid[r][c])
                row.append(max_val)
            maxLocal.append(row)

        return maxLocal
