# Explanation of Binary Search Tree (BST) Common Node Finder

This Python code is designed to find and print the common nodes in two Binary Search Trees (BSTs). A BST is a binary tree with a specific structure where the left subtree contains nodes with values less than the root, and the right subtree contains nodes with values greater than the root.

## Class: Solution

The code defines a class named `Solution`, which contains two methods for common node retrieval.

### `inOrderTraversal(self, root, result)`

- This method performs an in-order traversal of a binary tree.
- Parameters:
  - `root`: The root node of the tree being traversed.
  - `result`: A list that stores elements in the order they are traversed.
- In in-order traversal, the left subtree is explored first, followed by the current node, and then the right subtree.

### `findCommon(self, root1, root2)`

- This method finds common nodes in two BSTs.
- Parameters:
  - `root1`: The root node of the first BST.
  - `root2`: The root node of the second BST.
- The method accomplishes this by following these steps:
  1. Perform in-order traversal on the first BST (`root1`) and store the elements in `result1`.
  2. Perform in-order traversal on the second BST (`root2`) and store the elements in `result2`.
  3. Initialize two pointers, `i` and `j`, to 0.
  4. Create an empty list called `common_elements` to store the common nodes.
  5. Compare elements from `result1` and `result2` while advancing the pointers:
     - If the elements are equal, add the element to `common_elements`, and advance both `i` and `j`.
     - If the element in `result1` is smaller, advance `i`.
     - If the element in `result2` is smaller, advance `j`.
  6. Return `common_elements` as the result of common nodes.

## Driver Code

The driver code handles input and output and demonstrates the functionality of the `Solution` class. Here's how it works:

- Read the number of test cases, `t`.
- For each test case:
  - Read two lines of input, each representing a BST.
  - Build two BSTs (`root1` and `root2`) based on the input using the `buildTree` function.
  - Create an instance of the `Solution` class, `ob`.
  - Call the `findCommon` method to find common elements in the two BSTs.
  - Print the common elements for the current test case.

The code assumes that the input BSTs are well-formed and do not contain duplicate values. It employs in-order traversal to generate sorted lists of elements from each BST and then identifies common elements by comparing these lists element by element.

This code is useful for finding shared elements in two BSTs, which can be a valuable operation in various applications involving binary trees.
