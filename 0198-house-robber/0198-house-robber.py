class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev2,prev1=0,0
        for money in nums:
            curr=max(prev2+money,prev1)
            prev2=prev1
            prev1=curr
        return prev1
        