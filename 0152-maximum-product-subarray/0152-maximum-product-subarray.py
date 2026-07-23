class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro=nums[0]
        min_pro=nums[0]
        ans=nums[0]
        for num in nums[1:]:
            if num<0:
                max_pro,min_pro=min_pro,max_pro
            max_pro=max(num,num*max_pro)
            min_pro=min(num,num*min_pro)
            ans=max(ans,max_pro)
        return ans

        