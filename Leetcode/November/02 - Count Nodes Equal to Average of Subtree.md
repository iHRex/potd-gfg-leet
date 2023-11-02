

## 04. Average Value of Binary Tree Subtree

The problem can be found at the following link: [Question Link](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)

![](https://badgen.net/badge/Level/Medium/yellow)

The code is designed to calculate and return the average value of all the nodes in a binary tree.

### My Approach
1. **Depth-First Search (DFS)**: The code uses a depth-first search (DFS) approach to traverse the binary tree. The DFS function, `dfs`, is a recursive function that traverses the tree in a depth-first manner.

2. **Recursive DFS Function**: The `dfs` function takes a `node` as input, which represents the current node in the tree. It returns a list containing three values:
   - The sum of values in the subtree rooted at the current node (`left[0]+right[0]+node.val`).
   - The number of nodes in the subtree rooted at the current node (`left[1]+right[1]+1`).
   - The number of nodes whose average value is equal to the value of the current node (`left[2]+right[2]+int((left[0]+right[0]+node.val)//(left[1]+right[1]+1) == node.val)`).

3. **Return Result**: The function `dfs(root)[2]` returns the value of the third element in the list returned by the `dfs` function. This value represents the number of nodes whose average value is equal to the value of the root node.

4. **Overall Logic**: The code traverses the entire binary tree using the DFS approach. For each node, it calculates the sum of values and the number of nodes in the subtree rooted at that node. It also checks how many nodes in the subtree have an average value equal to the value of the current node.

5. **Result**: The final result is the number of nodes in the tree whose average value matches the value of the root node.

### Time and Space Complexity

- **Time Complexity**: O(n), where `n` is the number of nodes in the binary tree. The code visits each node once.
- **Space Complexity**: O(h), where `h` is the height of the binary tree. The code uses the call stack for recursive function calls, and the maximum depth of the call stack is the height of the tree.

### Code (Python)
```python
class Solution(object):
    def averageOfSubtree(self, root):
        def dfs(node):
            if not node:
                return [0]*3
            left = dfs(node.left)
            right = dfs(node.right)
            return [left[0]+right[0]+node.val,
                    left[1]+right[1]+1,
                    left[2]+right[2]+int((left[0]+right[0]+node.val)//(left[1]+right[1]+1) == node.val)]
        
        return dfs(root)[2]
```

### Contribution and Support

For discussions, questions, or doubts related to this solution, please visit our [discussion section](https://github.com/iHRex/potd-gfg-leet/discussions/). We welcome your input and aim to foster a collaborative learning environment.

If you find this solution helpful, consider supporting us by giving a ⭐ star to the [iHRex/potd-gfg-leet](https://github.com/iHRex/potd-gfg-leet) repository.
