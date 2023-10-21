# PROBLEM STATEMENT
## Constrained Subsequence Sum

Given an integer array `nums` and an integer `k`, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied.

_A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order._
 

Example 1:
```
Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
```
Example 2:
```
Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
```
Example 3:
```
Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
```
 

Constraints:


-   ``1 <= k <= nums.length <= 10^5``
-   `10^4 <= nums[i] <= 10^4`


 

<h3>Follow up:</h3> Can you solve it in O(n) time and O(1) space?
<br>
<br>









# Solution and Explanation of ``Constrained Subsequence Sum``


The `constrainedSubsetSum` function is designed to find the maximum sum of non-empty subarrays in the given array `nums` with a constraint. The constraint specifies that the selected elements in the subarray must be at most `k` indices apart.

## Function Signature
```java
public int constrainedSubsetSum(int[] nums, int k)
```

- `nums`: An array of integers in which we need to find the constrained subset.
- `k`: An integer representing the constraint on the maximum separation between elements in the subarray.

## Algorithm

The function uses dynamic programming and a deque (double-ended queue) to efficiently find the maximum sum of constrained subarrays.

- Initialize the array `dp` to store the maximum sum of subarrays ending at each position in the input array `nums`. Also, initialize `ans` to store the final answer, initially set to `Integer.MIN_VALUE`.

- Initialize a deque `q` to keep track of candidate indices that could contribute to the maximum sum.

- Iterate through the elements of the `nums` array using the index variable `i`:
    - Check if the deque `q` is not empty and the distance between the current index `i` and the index at the front of the deque (`q.peek()`) is greater than `k`. If so, remove elements from the front of the deque until the constraint is satisfied (`q.poll()`).

    - Calculate the maximum sum of the subarray ending at the current index `i` (`dp[i]`). The maximum sum can be calculated as the maximum of two values:
        - The maximum sum of the subarray ending at the index in the deque's front (if the deque is not empty), but ensuring it's non-negative (`Math.max(0, q.isEmpty() ? 0 : dp[q.peek()])`).
        - The value of the current element `nums[i]`.

    - While the deque `q` is not empty and the maximum sum of the subarray at the index in the deque's back (`dp[q.peekLast()]`) is less than or equal to the maximum sum at the current index (`dp[i]`), remove elements from the back of the deque (`q.pollLast()`).

    - Add the current index `i` to the deque (`q.offer(i)`).

    - Update the answer `ans` with the maximum sum found among all subarrays.

- After processing all elements in the `nums` array, the variable `ans` contains the maximum sum of constrained subarrays.

- Return `ans` as the result of the function.

## Conclusion

The `constrainedSubsetSum` function efficiently finds the maximum sum of non-empty subarrays in the given array `nums` while adhering to the constraint that the selected elements must be at most `k` indices apart. This algorithm is implemented using dynamic programming and a deque to optimize the computation.
