class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*n
        d=deque([source])
        visited[source]=True
        while d:
            u1=d.popleft()
            if u1==destination:
                return True
            for node in graph[u1]:
                if not visited[node]:
                    visited[node] = True
                    d.append(node)
        return False
        
        