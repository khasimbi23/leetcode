class Solution:
    def isPalindrome(self, s: str) -> bool:
        f="" 
        for ch in s:
            if ch.isalnum():
                f+=ch.lower()
        return f==f[::-1]