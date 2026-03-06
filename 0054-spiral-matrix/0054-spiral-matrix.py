class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        l=0
        r=len(matrix[0])-1
        t=0
        b=len(matrix)-1
        while t<=b and l<=r:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t=t+1
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r=r-1
            if t<=b:
                for i in range(r,l-1,-1):
                    res.append(matrix[b][i])
                b=b-1
            if l<=r:
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l=l+1
        return res


        