class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        idx=0
        i=0
        while i<n:
            ch=chars[i]
            c=0
            while i<n and chars[i]==ch:
                c+=1
                i+=1
            if c==1:
                chars[idx]=ch
                idx+=1
            else:
                chars[idx]=ch
                idx+=1
                for digit in str(c):
                    chars[idx]=digit
                    idx+=1
        chars[:]=chars[:idx]
        return idx

        