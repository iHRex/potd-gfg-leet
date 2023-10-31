#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	left = 0
        right = 0
        while right < n:
            if arr[right] != 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
            right += 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends