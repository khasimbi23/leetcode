class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mb={}
        for i in range(len(numbers)):
            b=target-numbers[i]
            if b in mb:
                return[mb[b],i+1]
            mb[numbers[i]]=i+1