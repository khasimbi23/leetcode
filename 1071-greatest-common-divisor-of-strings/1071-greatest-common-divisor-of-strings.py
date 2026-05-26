class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a,b):
            while(a>0 and b>0):
                if a>b:
                    a=a%b
                else:
                    b=b%a
            if a==0:
                return b
            else:
                return a
        if str1+str2 != str2+str1:
            return ""
        x=gcd(len(str1),len(str2))
        return str1[0:x]