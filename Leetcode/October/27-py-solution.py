class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (right-left+1)-2
        
        left, right = -1, -2
        for i in xrange(len(s)):
            l = max(expand(s, i, i), expand(s, i, i+1))
            if l > right-left+1:
                right = i+l//2
                left = right-l+1
        return s[left:right+1] if left >= 0 else ""