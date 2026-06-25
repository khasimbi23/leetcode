from heapq import *
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        grid=[[float('inf')]*n for i in range(m)]
        grid[0][0]=0
        minheap=[(0,0,0)] #diff,r,c
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        while minheap:
            diff,r,c = heapq.heappop(minheap)
            if diff>grid[r][c]:
                continue
            if r==m-1 and c==n-1:
                return diff
            for dr,dc in d:
                nr,nc = dr+r,dc+c
                if 0<=nr<m and 0<=nc<n:
                    newdiff=max(abs(heights[nr][nc]-heights[r][c]),diff)
                    if newdiff<grid[nr][nc]:
                        grid[nr][nc]=newdiff
                        heappush(minheap,(newdiff,nr,nc))
        return grid[m-1][n-1]



        