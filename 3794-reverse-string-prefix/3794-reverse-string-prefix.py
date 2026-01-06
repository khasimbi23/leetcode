class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        s[:k] = s[:k][::-1]
        return ''.join(s)

        