class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for num in range(left,right+1):
            temp=num
            valid=True
            while temp>0:
                dig=temp%10
                if dig==0 or num%dig!=0:
                    valid=False
                    break
                temp //= 10
            if valid:
                res.append(num)
        return res
        