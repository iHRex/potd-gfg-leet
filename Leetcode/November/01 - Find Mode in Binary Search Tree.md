
## 01. Mode in Binary Search Tree
The problem can be found at the following link: [Question Link](https://leetcode.com/problems/find-mode-in-binary-search-tree)

![](https://badgen.net/badge/Level/Easy/green)

### My Approach

This code finds the mode (most frequently occurring elements) in a Binary Search Tree (BST) using an in-order traversal approach. The following is a step-by-step explanation of how it works:

1. **Initialization**: The code starts by defining an `inorder` function for in-order traversal of the BST. It takes parameters such as the current `root`, the previous node `prev`, the current count `cnt`, the maximum count `max_cnt` seen so far, and a list `result` to store mode values.

2. **In-Order Traversal**: The `inorder` function recursively traverses the BST. The process includes the following steps:
   - If the current node `root` is `None`, the function returns the values of `prev`, `cnt`, and `max_cnt`.
   - The in-order traversal begins by calling `inorder` on the left child (recursion).
   - It checks if the value of the current node `root.val` is equal to the value of the previous node `prev.val`. If they are equal, it increments `cnt` to count consecutive occurrences of the same value. If they are different, it resets `cnt` to 1.
   - It then compares the value of `cnt` to the value of `max_cnt`. If `cnt` is greater, it updates `max_cnt` to `cnt` and clears the `result` list. The current value `root.val` is appended to the `result`.
   - If `cnt` is equal to `max_cnt`, it means another mode value is found, so the current value is appended to the `result` as well.
   - The function proceeds to the right child (recursion), updating `prev`, `cnt`, and `max_cnt` accordingly.

3. **Main Code**: After defining the `inorder` function, the main part of the code checks if the BST's `root` is not empty.

4. **Initialization of Result**: If the `root` is not empty, it initializes an empty `result` list to store the mode values.

5. **In-Order Traversal Call**: It then calls the `inorder` function to start the in-order traversal. The helper function initializes `prev` as `None`, `cnt` as 1 (assuming the root is the first occurrence), and `max_cnt` as 0 (no modes found yet).

6. **Result**: Finally, the code returns the `result` list, which contains the mode values in the BST.

### Time and Space Complexity

- **Time Complexity**: O(N), where N is the number of nodes in the BST, as it traverses all nodes once.
- **Space Complexity**: O(H), where H is the height of the BST, as it uses a function call stack for the recursion.

### Code (Python)
```python
def findMode(root):
    def inorder(root, prev, cnt, max_cnt, result):
        # Implementation of the inorder function
        # ...
        return result
    if not root:
        return []
    result = []
    inorder(root, None, 1, 0, result)
    return result
```

### Contribution and Support

For discussions, questions, or doubts related to this solution, please visit our [discussion section](https://github.com/iHRex/potd-gfg-leet/discussions). We welcome your input and aim to foster a collaborative learning environment.

If you find this solution helpful, consider supporting us by giving a ⭐ star to the [iHRex/potd-gfg-leet](https://github.com/iHRex/potd-gfg-leet) repository.

