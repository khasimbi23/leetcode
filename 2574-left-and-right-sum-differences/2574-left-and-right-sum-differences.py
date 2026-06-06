class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        t_sum=sum(nums)
        l_sum=0
        ans=[]
        for num in nums:
            r_sum=t_sum-l_sum-num
            ans.append(abs(l_sum-r_sum))
            l_sum+=num
        return ans
        