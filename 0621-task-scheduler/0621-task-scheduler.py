class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=[0]*26
        for i in range(len(tasks)):
            freq[ord(tasks[i])-ord('A')]+=1
        maxif=max(freq)
        c=0
        for i in freq:
            if i==maxif:
                c+=1
        return max(len(tasks),(n+1)*(maxif-1)+c)
        