class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) 
        visit = []
        for i in range(n):
            visit.append([False] * m)       
        q = []
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and grid[i][j] == 1:
                    q.append([i, j])
                    visit[i][j] = True
        while q:
            t = q.pop(0)
            i, j = t[0], t[1]           
            child = [
                [i+1, j], [i-1, j],
                [i, j+1], [i, j-1]
            ]           
            for c in child:
                ci, cj = c[0], c[1]             
                if (ci >= 0 and ci < n and 
                    cj >= 0 and cj < m and 
                    not visit[ci][cj] and 
                    grid[ci][cj] == 1):
                    
                    visit[ci][cj] = True
                    q.append([ci, cj])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visit[i][j]:
                    count += 1
        
        return count