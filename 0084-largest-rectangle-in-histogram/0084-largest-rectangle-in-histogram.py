class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        heights.append(0)
        maxi = 0   
        for i in range(len(heights)):
            while st != [] and heights[st[-1]] >= heights[i]:
                ind = st.pop()
                ht = heights[ind]
                nsei = i
                psei = st[-1] if st != [] else -1
                wid = nsei - psei - 1
                area = ht * wid
                maxi = max(maxi, area)
            st.append(i)
        return maxi