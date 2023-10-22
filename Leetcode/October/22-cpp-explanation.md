# PROBLEM STATEMENT
## Maximum Score of a Good Subarray

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray ``(i, j)`` is defined as ``min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1)``. A good subarray is a subarray where ``i <= k <= j``.

_Return the maximum possible <b>score</b> of a <b>good</b> subarray._
 

Example 1:
```
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
```
Example 2:
```
Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
```

 

Constraints:


-   ``1 <= nums.length <= 10^5``
-   ``1 <= nums[i] <= 2 * 104``
-   ``0 <= k < nums.length``


 

<h3>Follow up:</h3> Can you solve it in O(n) time and O(1) space?
<br>
<br>









# Solution and Explanation of ``Maximum Score of a Good Subarray``


## Explanation of `maximumScore` Function

The `maximumScore` function calculates the maximum score achievable by selecting a subarray from the given array `nums`. The score of a subarray is defined as the minimum element in the subarray multiplied by the length of the subarray. The function is designed to find the maximum possible score by choosing the optimal subarray.

## Function Signature
```cpp
int maximumScore(vector<int>& nums, int k)
```

- `nums`: A vector of integers representing the input array.
- `k`: An integer indicating the index at which the subarray should be centered.

## Algorithm

1. Calculate the maximum score for a subarray centered at index `k`. This is done by invoking the `score` function with the original `nums` and the index `k`. Store the result in a variable `result`.

2. Reverse the `nums` array using the `reverse` function. This is done to calculate the maximum score when centering the subarray at index `size(nums) - k - 1`.

3. Calculate the maximum score for a subarray centered at index `size(nums) - k - 1`. This is done by invoking the `score` function with the reversed `nums` and the index `size(nums) - k - 1`. Take the maximum of the previous `result` and this new score to determine the overall maximum score.

## `score` Function

The `score` function calculates the maximum score of a subarray centered at index `k`.

1. Initialize an array `prefix` of size `k + 1` and initialize the first element with `nums[k]`. This array is used to store the prefix minimum values for subarrays of different lengths.

2. Iterate from `k - 1` to `0`:
   - For each index `i`, calculate the prefix minimum for subarrays of length `k - i + 1`. Store this minimum value in the `prefix` array.

3. Initialize the variables `result` and `right` with `nums[k]`. These variables are used to keep track of the maximum score and the right minimum value as the subarray extends.

4. Iterate from `k` to `size(nums)`:
   - For each index `j`, update the right minimum value by taking the minimum of the current `right` and `nums[j]`.
   - Find the index `i` in the `prefix` array where the value is greater than or equal to the current `right`. This is done using the `lower_bound` function and calculating the distance from the beginning of the `prefix` array.
   - If `i` is not equal to the size of the `prefix` array, calculate a potential score by multiplying `right` by `(j - i + 1)`, which represents the length of the subarray from `i` to `j`. Update the `result` with the maximum of the current `result` and the potential score.

5. Return the `result` as the maximum score for a subarray centered at index `k`.

## Conclusion

The `maximumScore` function efficiently calculates the maximum score for a subarray centered at index `k` in the given input array `nums`. It accomplishes this by invoking the `score` function for two possible subarray centers (original and reversed) and selecting the maximum score. The `score` function finds the maximum score by considering the minimum value in each subarray and its length, ensuring an optimal solution.