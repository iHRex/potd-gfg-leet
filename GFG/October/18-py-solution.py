#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        def isSafeNode(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1  # Mark the node as visiting.

            for neighbor in adj[node]:
                if not isSafeNode(neighbor):
                    return False  # If any neighbor is not safe, the current node is not safe.

            visited[node] = 2  # Mark the node as visited and safe.
            return True

        result = []
        visited = [0] * V  # 0: unvisited, 1: visiting, 2: visited

        for i in range(V):
            if isSafeNode(i):
                result.append(i)

        return sorted(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends