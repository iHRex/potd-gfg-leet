## Problem Statement

The code aims to find the greatest value node in a Binary Search Tree (BST) that is smaller than or equal to a given value 'x'. In a BST, each node has two child nodes: a left child with a smaller value and a right child with a greater value than the parent node.

## Code Explanation

```cpp
// Function to search a node in BST.
class Solution {
public:
    int floor(Node* root, int x) {
        int floorValue = -1;  // Initialize floorValue to -1.
        
        while (root != NULL) {  // Iterate through the BST nodes.
            if (root->data == x) {
                return x;  // If the current node's data is equal to 'x', return 'x'.
            } else if (root->data < x) {  // If the current node's data is less than 'x':
                floorValue = root->data;  // Update floorValue with the current node's data.
                root = root->right;  // Move to the right subtree.
            } else {
                root = root->left;  // If the current node's data is greater than 'x', move to the left subtree.
            }
        }
        
        return floorValue;  // Return the greatest value smaller than or equal to 'x' found in the BST.
    }
};
```

### Detailed Explanation

1. The `floor` function takes two parameters: the root of a BST (`Node* root`) and an integer value `x`.

2. It initializes `floorValue` to -1. This variable will keep track of the greatest value in the BST that is smaller than or equal to 'x'.

3. The code enters a `while` loop that iterates through the BST nodes as long as the `root` is not `NULL`.

4. Inside the loop, it checks if the data of the current node (`root->data`) is equal to 'x'. If it is, the function returns 'x' because it has found the exact value in the BST.

5. If the current node's data is less than 'x', it means that the current node could be a candidate for the floor value. It updates `floorValue` with the current node's data and then moves to the right subtree (`root = root->right`) to explore larger values.

6. If the current node's data is greater than 'x', it means that the desired floor value should be in the left subtree. The code moves to the left subtree (`root = root->left`) to explore smaller values.

7. The function continues this process until it reaches a leaf node or until it finds an exact match. At the end, it returns `floorValue`, which contains the greatest value in the BST smaller than or equal to 'x'.

## Driver Code

The driver code initializes a BST, inserts values into it, and calls the `floor` function for each test case.

The code follows a standard input/output approach, where it reads the number of test cases, constructs the BST, and then prints the floor value for each test case.

This explanation provides a detailed breakdown of how the code works to find the floor value in a Binary Search Tree.