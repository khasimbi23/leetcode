class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=j=0
        g.sort()
        s.sort()
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
            j+=1
        return i
