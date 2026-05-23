class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def rev(st,en):
            while(st<en):
                nums[st],nums[en]=nums[en],nums[st]
                st=st+1
                en=en-1
        rev(0,len(nums)-1)
        rev(0,k-1)
        rev(k,len(nums)-1 )
        