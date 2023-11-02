# 02. Minimum Distance Between Two Numbers in an Array

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1)

![](https://badgen.net/badge/Level/Easy/green)

The code is designed to find the minimum distance between two specified numbers, `x` and `y`, in an array. The code uses a linear approach to scan the array and calculate the minimum distance between occurrences of `x` and `y`.

### My Approach

1. **Initialization**: The code begins by initializing three variables: `last_x_index`, `last_y_index`, and `min_distance`. 
   - `last_x_index` and `last_y_index` store the indices of the last occurrences of `x` and `y`, respectively, and are initialized to -1, indicating that they haven't been seen yet.
   - `min_distance` is set to positive infinity (`float('inf')`) to ensure that any calculated distance will be smaller than its initial value.

2. **Iterating Through the Array**: The code iterates through the given array from the start to the end (index `i`). Inside the loop:
   - If the current element in the array (`arr[i]`) is equal to `x`, the code checks if `last_y_index` is not equal to -1. If it is not -1, it means that `y` has been seen before. In this case, the code calculates the distance between the current index `i` and the last occurrence of `y` (`last_y_index`) and updates `min_distance` if the calculated distance is smaller.
   - The index `last_x_index` is updated to the current index `i` as the last occurrence of `x`.

   - Similarly, if `arr[i]` is equal to `y`, the code checks if `last_x_index` is not equal to -1. If it is not -1, it means that `x` has been seen before. In this case, the code calculates the distance between the current index `i` and the last occurrence of `x` (`last_x_index`) and updates `min_distance` if the calculated distance is smaller.
   - The index `last_y_index` is updated to the current index `i` as the last occurrence of `y`.

3. **Final Check**: After the loop, the code checks if either `last_x_index` or `last_y_index` is still equal to -1. This would mean that one of the two numbers (`x` or `y`) was not found in the array. If this is the case, the code returns -1, indicating that it's not possible to calculate the minimum distance as both `x` and `y` must be present in the array.

4. **Result**: If both `x` and `y` were found in the array, the code returns the calculated `min_distance`, which represents the minimum distance between the occurrences of `x` and `y` in the array.

### Time and Space Complexity

- **Time Complexity**: O(n), where n is the size of the array. The code iterates through the array once.
- **Space Complexity**: O(1), as the code uses a constant amount of extra space for variables.

### Code (Python)
```python
def minDistance(arr, x, y):
    last_x_index = -1
    last_y_index = -1
    min_distance = float('inf')

    for i in range(len(arr)):
        if arr[i] == x:
            if last_y_index != -1:
                min_distance = min(min_distance, i - last_y_index)
            last_x_index = i
        elif arr[i] == y:
            if last_x_index != -1:
                min_distance = min(min_distance, i - last_x_index)
            last_y_index = i

    if last_x_index == -1 or last_y_index == -1:
        return -1

    return min_distance
```

### Contribution and Support

For discussions, questions, or doubts related to this solution, please visit our [discussion section](https://github.com/iHRex/potd-gfg-leet/discussions). We welcome your input and aim to foster a collaborative learning environment.

If you find this solution helpful, consider supporting us by giving a ⭐ star to the [iHRex/potd-gfg-leet](https://github.com/iHRex/potd-gfg-leet) repository.
