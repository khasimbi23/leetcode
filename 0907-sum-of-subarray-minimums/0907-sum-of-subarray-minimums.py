class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        pse_ind=[-1]*len(arr)
        st=[]
        for i in range(0,len(arr)):
            while st!=[] and arr[st[-1]]>=arr[i]:
                st.pop()
            if st!=[]:
                pse_ind[i]=st[-1]
            st.append(i)
        nse_ind=[len(arr)]*len(arr)
        st=[]
        for i in range(len(arr)-1,-1,-1):
            while st!=[] and arr[st[-1]]>arr[i]:
                st.pop()
            if st!=[]:
                nse_ind[i]=st[-1]
            st.append(i)
        s=0
        mod=10**9+7
        for i in range(len(arr)):
            count=(i-pse_ind[i])*(nse_ind[i]-i)
            contribution=arr[i]*count
            s=(s+contribution)%mod
        return s%mod
            

        