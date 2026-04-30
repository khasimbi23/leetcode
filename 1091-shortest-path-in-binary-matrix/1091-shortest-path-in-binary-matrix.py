from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])   # FIX: define m
        
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        
        start = [0, 0]
        
        visit = []
        for i in range(n):
            visit.append([False] * m)   # FIX: m defined
        
        q = []
        q.append(start)
        visit[0][0] = True
        
        level = 0
        
        while q:
            l = len(q)
            level += 1
            
            for k in range(l):
                t = q.pop(0)
                i, j = t[0], t[1]
                
                # FIX: correct destination condition
                if i == n-1 and j == m-1:
                    return level
                
                # FIX: correct children list
                child = [
                    [i+1, j], [i-1, j],
                    [i, j+1], [i, j-1],
                    [i+1, j+1], [i+1, j-1],
                    [i-1, j+1], [i-1, j-1]
                ]
                
                for c in child:
                    ci, cj = c[0], c[1]
                    
                    if (ci >= 0 and ci < n and 
                        cj >= 0 and cj < m and 
                        not visit[ci][cj] and 
                        grid[ci][cj] == 0):
                        
                        visit[ci][cj] = True
                        q.append([ci, cj])
        
        return -1