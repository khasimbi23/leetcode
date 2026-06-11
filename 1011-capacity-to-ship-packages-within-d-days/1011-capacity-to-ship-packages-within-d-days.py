class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            curr_day=1
            curr_load=0
            for weight in weights:
                if curr_load+weight>capacity:
                    curr_day+=1
                    curr_load=weight
                else:
                    curr_load+=weight
            return curr_day<=days
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=(left+right)//2
            if can_ship(mid):
                right=mid
            else:
                left=mid+1
        return left 
        