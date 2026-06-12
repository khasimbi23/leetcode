class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five =0
        ten=0
        for coin in bills:
            if coin==5:
                five+=1
            elif coin==10:
                ten+=1
                if five ==0:
                    return False
                else:
                    five-=1
            else:
                if ten>0 and five >0:
                    ten-=1
                    five-=1
                elif five>2:
                    five-=3
                else:
                    return False
        return True