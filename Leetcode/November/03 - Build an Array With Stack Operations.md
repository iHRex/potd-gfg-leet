# 03. Build an Array With Stack Operations
The problem can be found at the following link: [Question Link](https://leetcode.com/problems/build-an-array-with-stack-operations)

![](https://badgen.net/badge/Level/Medium/yellow)

The code is designed to create a sequence of stack operations to transform an empty array into a target array.

### My Approach
1. **Iterative Approach**: The code utilizes an iterative approach to generate the sequence of stack operations.
   - It initializes two lists: `result` to store the stack operations and `curr` to keep track of the current element we want to reach in the target array.
   - It iterates through the elements in the `target` array.
   - For each element `t` in `target`, it calculates the difference between `t` and `curr`. For every `x` in this difference:
     - It adds "Push" to `result`.
     - It adds "Pop" to `result`.
   - After handling the difference, it appends "Push" to `result` to reach the `t` element.
   - It updates `curr` to `t + 1` to set the next expected element.

2. **Return Result**: The code returns the list of stack operations stored in the `result` list, which represents the sequence to transform the empty array into the target array.

### Time and Space Complexity
- **Time Complexity**: O(n), where `n` is the size of the `target` array. The code iterates through the `target` array and generates the stack operations.
- **Space Complexity**: O(1), as the `result` and `curr` lists do not depend on the size of the input data.

### Code (Python)
```python
class Solution(object):
    def buildArray(self, target, n):
        result, curr = [], 1
        for t in target:
            result.extend(["Push", "Pop"] * (t - curr))
            result.append("Push")
            curr = t + 1
        return result
```

### Contribution and Support

For discussions, questions, or doubts related to this solution, please visit our [discussion section](https://github.com/iHRex/potd-gfg-leet/discussions/). We welcome your input and aim to foster a collaborative learning environment.

If you find this solution helpful, consider supporting us by giving a ⭐ star to the [iHRex/potd-gfg-leet](https://github.com/iHRex/potd-gfg-leet) repository..