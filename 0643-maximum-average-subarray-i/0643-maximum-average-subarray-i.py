class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        maxi=float('-inf')
        for i in range(0,k):
            s=s+nums[i]
        maxi=s
        for i in range(k,len(nums)):
            s=s+nums[i]-nums[i-k]
            maxi=max(maxi,s)
        return maxi/k

        
        