#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
		# code here
        max_sum = [0] * n

        for i in range(n):
            max_sum[i] = Arr[i]
            
        for i in range(1, n):
            for j in range(i):
                if Arr[i] > Arr[j] and max_sum[i] < max_sum[j] + Arr[i]:
                    max_sum[i] = max_sum[j] + Arr[i]

        max_sequence_sum = max(max_sum)

        return max_sequence_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends