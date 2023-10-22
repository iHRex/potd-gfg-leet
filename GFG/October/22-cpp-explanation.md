<img align="center" alt="Medium" height=100 widhth=100   src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/GeeksforGeeks.svg/1200px-GeeksforGeeks.svg.png"/>

# Problem Statement

## Number of paths

The problem is to count all the possible paths from top left to bottom right of an `MxN`` matrix with the constraints that from each cell you can either move to <b>right</b> or <b>down</b>.

Return answer modulo (10<sup>9</sup>)+7

### Example 1:


```
Input:
M = 3 and N = 3
Output: 6
Explanation:
Let the given input 3*3 matrix is filled 
as such:
A B C
D E F
G H I
The possible paths which exists to reach 
'I' from 'A' following above conditions 
are as follows:ABCFI, ABEHI, ADGHI, ADEFI, 
ADEHI, ABEFI
```

### Example 2:

```
Input:
M = 1 and N = 4
Output: 1
Explanation:
There is only one direction to go in,
and thus, there is only one path possible.
```

### Your task:
You don't need to read input or print anything. Your task is to complete the function numberOfPaths() which takes the integer M and integer N as input parameters and returns an integer, the number of paths.


##### Expected Time Complexity: O(M)

##### Expected Auxiliary Space: O(1)

Constraints:
```
1 ≤ N ≤ 10^8
1 ≤ M ≤ 10^5
```

___
___




# Solution Statement and Explanation of `Number of paths`

The `numberOfPaths` function is designed to calculate the number of unique paths from the top-left corner to the bottom-right corner of an `m x n` grid. The paths are allowed to move only in two directions: right and down.

## Function Signature
```cpp
long long numberOfPaths(int m, int n)
```

- `m`: An integer representing the number of rows in the grid.
- `n`: An integer representing the number of columns in the grid.

## Algorithm

The function calculates the number of paths using a combinatorial approach. It uses modular arithmetic to avoid integer overflow for large inputs.

1. Initialize a variable `out` to store the result. Also, initialize a variable `mod` as `1e9 + 7` for performing modular arithmetic.

2. Create a helper function `modInv` that calculates the modular multiplicative inverse of an integer. This helper function is used later to perform division under modulo.

3. Iterate from `i = 0` to `i = m - 2`:
   - Calculate the modular inverse of `(i + 1)` using the `modInv` function.
   - Update the `out` value as follows:
     - Multiply `out` by `(i + n)` and take the result modulo `mod`.
     - Multiply the result by the modular inverse of `(i + 1)` and take the result modulo `mod`.

4. After the loop, the `out` variable contains the number of unique paths from the top-left corner to the bottom-right corner.

5. Return `out` as the result of the function.

## Conclusion

The `numberOfPaths` function calculates the number of unique paths in an `m x n` grid using a combinatorial approach with modular arithmetic. This algorithm efficiently handles large inputs and provides the correct count of unique paths.