class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True
class Solution:
    def maxStability(self, n, edges, k):
        def can(x):
            dsu = DSU(n)
            used = 0
            upgrades = 0
            for u, v, s, must in edges:
                if must == 1:
                    if s < x:
                        return False
                    if not dsu.union(u, v):
                        return False   
                    used += 1
            optional = []
            for u, v, s, must in edges:
                if must == 0:
                    optional.append((u, v, s))
            optional.sort(key=lambda e: -e[2])
            for u, v, s in optional:
                if used == n - 1:
                    break
                if dsu.find(u) != dsu.find(v):
                    if s >= x:
                        dsu.union(u, v)
                        used += 1
                    elif s * 2 >= x and upgrades < k:
                        dsu.union(u, v)
                        upgrades += 1
                        used += 1
            return used == n - 1
        lo = 0
        hi = max(s for _, _, s, _ in edges) * 2
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans