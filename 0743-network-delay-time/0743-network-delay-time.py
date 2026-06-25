import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        minheap = [(0, k)]
        while minheap:
            t, node = heapq.heappop(minheap)
            if t > dist[node]:
                continue
            for nei, wt in adj[node]:
                if t + wt < dist[nei]:
                    dist[nei] = t + wt
                    heapq.heappush(minheap, (dist[nei], nei))
        res = max(dist[1:])
        return res if res != float('inf') else -1