from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        distance = [float('inf')] * n
        distance[src] = 0
        queue = deque([(src, 0)])
        stops = 0
        while queue and stops <= k:
            for _ in range(len(queue)):
                node, weight = queue.popleft()
                for nei, nwt in adj[node]:
                    if weight + nwt < distance[nei]:
                        distance[nei] = weight + nwt
                        queue.append((nei, distance[nei]))
            stops += 1
        return distance[dst] if distance[dst] != float('inf') else -1