class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        st=[]
        end=[]
        for i,j in flowers:
            st.append(i)
            end.append(j)
        st.sort()
        end.sort()
        res=[]
        for time in people:
            started=bisect_right(st,time)
            ended=bisect_left(end,time)
            diff=started-ended
            res.append(diff)
        return res