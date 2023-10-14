#Find Common Nodes in two BSTs
#Given two Binary Search Trees. Find the nodes that are common in both of them, ie- find the intersection of the two BSTs.

#User function Template for python3


class Solution:
    
    #Function to find the nodes that are common in both BST.
    def inOrderTraversal(self, root, result):
        if root:
            self.inOrderTraversal(root.left, result)
            result.append(root.data)
            self.inOrderTraversal(root.right, result)
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        # code here
        result1, result2 = [], []
        
        # Perform in-order traversal on the first BST and store the elements in result1.
        self.inOrderTraversal(root1, result1)
        
        # Perform in-order traversal on the second BST and store the elements in result2.
        self.inOrderTraversal(root2, result2)
        
        # Initialize pointers for both lists.
        i, j = 0, 0
        common_elements = []

        # Compare the elements in the two lists while advancing the pointers.
        while i < len(result1) and j < len(result2):
            if result1[i] == result2[j]:
                common_elements.append(result1[i])
                i += 1
                j += 1
            elif result1[i] < result2[j]:
                i += 1
            else:
                j += 1
        
        return common_elements
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root1=buildTree(s)
        s=input()
        root2=buildTree(s)
        ob = Solution()
        res = ob.findCommon(root1, root2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends