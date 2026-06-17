class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # using queue data structure
        d=deque(range(1,n+1))
        while len(d)>1:
            for i in range(k-1):
                x=d.popleft()
                d.append(x)
            d.popleft()
        return d[0]
        