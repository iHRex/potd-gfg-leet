
## 01. Find Mode in Binary Search Tree
The problem can be found at the following link: [Question Link](https://leetcode.com/problems/find-mode-in-binary-search-tree)

![](https://badgen.net/badge/Level/Easy/green)


### My Approach

This code finds the mode (most frequently occurring elements) in a Binary Search Tree (BST) using an in-order traversal approach. Here's a detailed explanation of how it works:

1. **Initialization**: The code starts by defining the `inorder` function for in-order traversal of the BST. This function takes several parameters: `root` (current node), `prev` (previous node), `cnt` (count of consecutive elements), `max_cnt` (maximum count seen so far), and `result` (list to store mode values).

2. **In-Order Traversal**: The `inorder` function recursively traverses the BST following these steps:
   - If the current node `root` is `None`, it returns the values of `prev`, `cnt`, and `max_cnt`.
   - The in-order traversal starts by calling `inorder` on the left child (recursion).
   - It checks if the value of the current node `root.val` is equal to the value of the previous node `prev.val`. If they are equal, it increments `cnt` to count consecutive occurrences of the same value. If they are different, it resets `cnt` to 1.
   - It then compares the value of `cnt` to the value of `max_cnt`. If `cnt` is greater, it updates `max_cnt` to `cnt`, clears the `result` list, and appends the current value `root.val`.
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
        if not root:
            return prev, cnt, max_cnt
        prev, cnt, max_cnt = inorder(root.left, prev, cnt, max_cnt, result)
        if prev:
            if root.val == prev.val:
                cnt += 1
            else:
                cnt = 1
        if cnt > max_cnt:
            max_cnt = cnt
            del result[:]
            result.append(root.val)
        elif cnt == max_cnt:
            result.append(root.val)
        return inorder(root.right, root, cnt, max_cnt, result)

    if not root:
        return []
    result = []
    inorder(root, None, 1, 0, result)
    return result
```




### Contribution and Support

For discussions, questions, or doubts related to this solution, please visit our [discussion section](https://github.com/iHRex/potd-gfg-leet/discussions). We welcome your input and aim to foster a collaborative learning environment.

If you find this solution helpful, consider supporting us by giving a ⭐ star to the [iHRex/potd-gfg-leet](https://github.com/iHRex/potd-gfg-leet) repository.

