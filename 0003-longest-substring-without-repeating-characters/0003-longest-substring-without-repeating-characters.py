class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            seen = set()
            length = 0 
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                length += 1  
            max_length = max(max_length, length)
        return max_length