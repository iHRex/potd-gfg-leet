<img align="center" alt="Medium" height=100 widhth=100   src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/GeeksforGeeks.svg/1200px-GeeksforGeeks.svg.png"/>

# Problem Statement

## Sum of all divisors from 1 to n
Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) for the number i is defined as the sum of all divisors of i.

### Example 1:


```
Input:
N = 4
Output:
15
Explanation:
F(1) = 1
F(2) = 1 + 2 = 3
F(3) = 1 + 3 = 4
F(4) = 1 + 2 + 4 = 7
ans = F(1) + F(2) + F(3) + F(4)
    = 1 + 3 + 4 + 7
    = 15
```

### Example 2:

```
Input:
N = 5
Output:
21
Explanation:
F(1) = 1
F(2) = 1 + 2 = 3
F(3) = 1 + 3 = 4
F(4) = 1 + 2 + 4 = 7
F(5) = 1 + 5 = 6
ans = F(1) + F(2) + F(3) + F(4) + F(5)
    = 1 + 3 + 4 + 7 + 6
    = 21
```

### Your task:
You don't need to read input or print anything. Your task is to complete the function sumOfDivisors() which takes an integer N as an input parameter and returns an integer.


##### Expected Time Complexity: O(N)

##### Expected Auxiliary Space: O(1)

Constraints:
```
1 <= N <= 10^6
```

___
___




# Solution Statement and Explanation of Sum of Divisors


## Introduction
The code is designed to calculate the sum of divisors of a given number ``N``. The sum of divisors refers to the sum of all positive integers that evenly divide the given number.

## `Solution` Class
```python
class Solution:
    def sumOfDivisors(self, N):
    	#code here 
        result = 0
        for i in range(1, N + 1):
            result += (N // i) * i
        return result
```

The `Solution` class contains a single method called `sumOfDivisors`, which computes the sum of divisors for a given number `N`.

### `sumOfDivisors` Method
- The `sumOfDivisors` method takes an integer `N` as input and returns the sum of divisors.
- It initializes `result` to 0, which will accumulate the sum of divisors.

To compute the sum of divisors, it iterates through all integers from `1` to `N` (inclusive).
- For each integer `i`, it calculates `(N // i) * i`, which represents the sum of divisors for which `i` is a divisor.
- This result is added to the `result` variable.
- Finally, the method returns the computed `result`, which is the sum of divisors of `N`.

## Driver Code
```python
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
```

The driver code reads the number of test cases `t` and iterates through each test case.
- For each test case, it reads the input value `N`.
- It creates an instance of the `Solution` class.
- Calls the `sumOfDivisors` method with the input value `N`.
- Prints the result, which is the sum of divisors for `N`.

This code efficiently calculates the sum of divisors for a given number and can be useful in various mathematical and programming tasks.