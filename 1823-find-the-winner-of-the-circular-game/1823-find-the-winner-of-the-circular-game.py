class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # using recursion
        def helper(n,k):
            if n==1:
                return 0
            return (helper(n-1,k)+k)%n
        return 1+helper(n,k)