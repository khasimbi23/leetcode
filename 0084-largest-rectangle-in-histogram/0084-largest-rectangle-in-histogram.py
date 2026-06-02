class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse_ind = [-1] * n
        st = []
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                pse_ind[i] = st[-1]
            st.append(i)
        nse_ind = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                nse_ind[i] = st[-1]
            st.append(i)
        max_area = 0
        for i in range(n):
            width = nse_ind[i] - pse_ind[i] - 1
            max_area = max(max_area, heights[i] * width)
        return max_area