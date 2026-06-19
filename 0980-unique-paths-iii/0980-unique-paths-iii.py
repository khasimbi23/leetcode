class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        empty_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 0:
                    empty_count += 1
        def backtrack(r, c, remaining):
            if grid[r][c] == 2:
                return 1 if remaining == -1 else 0
            temp = grid[r][c]
            grid[r][c] = -1
            paths = 0 
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                    paths += backtrack(nr, nc, remaining - 1)
            grid[r][c] = temp
            return paths  
        return backtrack(start_r, start_c, empty_count)