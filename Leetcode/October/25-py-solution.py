# Time  : O(1)
# Space : O(1)

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        def bitCount(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result

        return bitCount(k-1) % 2
