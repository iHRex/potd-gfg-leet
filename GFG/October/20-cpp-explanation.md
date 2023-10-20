<img align="center" alt="Medium" height=100 widhth=100   src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/GeeksforGeeks.svg/1200px-GeeksforGeeks.svg.png"/>

# Problem Statement

## Form a number divisible by 3 using array digits
You will be given an array arr of integers of length N. You can construct an integer from two integers by treating the integers as strings, and then concatenating them. For example, 19 and 4 can be used to construct 194 and 419.

The task is to find whether it’s possible to construct an integer using all the digits of these numbers such that it would be divisible by 3.
If it is possible then print 1 and if not print 0.

### Example 1:


```
Input: N = 3
arr = {40, 50, 90}
Output: 1
Explanation: One such number is 405090.
```

### Example 2:

```
Input: N = 2
arr = {1, 4}
Output: 0
Explanation: The numbers we can form 
are 14 and 41. But neither of them are 
divisible by 3.
```

### Your task:
You do not need to read input or print anything. Your task is to complete the function isPossible() which takes N and arr as input parameters and returns 1 if we can form a number by the digits of the given number, that would be divisible by 3, otherwise returns 0.

##### Expected Time Complexity: O(N)

##### Expected Auxiliary Space: O(1)

Constraints:
```
1 ≤ N, arr[i] ≤ 105
```

___
___




# Solution Statement and Explanation of Explanation of Code to Check if Sum is Divisible by 3 using array digits


## Introduction
The provided code is a C++ solution that determines whether the sum of the elements in an array is divisible by 3. It defines a class `Solution` with a function `isPossible` that takes an integer `N` (the number of elements in the array) and an array `arr` as input. The function returns `1` if the sum of the array elements is divisible by 3 and `0` otherwise.

## Function `isPossible`
```cpp
int isPossible(int N, int arr[]) {
    int sum = 0;
    for(int i=0; i<N; i++)
        sum += arr[i] % 3;
    return sum % 3 == 0;
}
```

- The function `isPossible` takes the length of the array `N` and the array `arr` as input.

- It initializes a variable `sum` to zero to store the sum of the array elements.

- It iterates through the elements of the array using a `for` loop, and for each element `arr[i]`, it calculates the remainder when divided by 3 (`arr[i] % 3`) and adds it to the `sum`. This step ensures that we consider only the remainder when summing the elements, not their absolute values.

- After calculating the sum of the remainders, the function checks if the `sum` is divisible by 3 by using the modulo operator (`sum % 3`). If the result is zero, it means that the original sum of the array elements is divisible by 3, so the function returns `1` (true). Otherwise, it returns `0` (false).

## Main Function
```cpp
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        int arr[N];
        for (int i = 0; i < N; i++) cin >> arr[i];

        Solution ob;
        cout << ob.isPossible(N, arr) << endl;
    }
    return 0;
}
```

- The main function reads an integer `t` representing the number of test cases.

- For each test case, it reads an integer `N`, the length of the array.

- It reads the elements of the array `arr` and stores them in the array.

- It creates an instance of the `Solution` class called `ob`.

- For each test case, it calls the `isPossible` function with the array length `N` and the array `arr` as arguments and prints the result.

- The main function iterates through all test cases and prints the results.

## Summary
The code efficiently checks if the sum of array elements is divisible by 3 by considering the remainders of individual elements. If the remainder-based sum is divisible by 3, the code returns `1`, indicating that the sum is divisible by 3; otherwise, it returns `0`. This code is designed to handle multiple test cases and provide results for each of them.


