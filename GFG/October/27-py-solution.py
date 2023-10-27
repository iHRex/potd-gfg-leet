#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here 
        n = len(S)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if S[i] == S[j] and cl == 2:
                    dp[i][j] = 2
                elif S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        lps_length = dp[0][n - 1]

        min_deletions = n - lps_length

        return min_deletions


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends