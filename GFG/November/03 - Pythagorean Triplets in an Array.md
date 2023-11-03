# 03. Pythagorean Triplets in an Array

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/pythagorean-triplet3018/1)

![](https://badgen.net/badge/Level/Medium/yellow)

The code is designed to find whether there exist any Pythagorean triplets in an array of integers. A Pythagorean triplet is a set of three positive integers `a`, `b`, and `c` such that `a^2 + b^2 = c^2`.

### My Approach
1. **Binary Search for Square Roots**: The code uses a binary search function `findroot` to find the square root of a given number `n`. It starts with a binary search range between `1` and `n`. The binary search continues until it converges to the largest integer whose square is less than or equal to `n`.

2. **Main Function**: The main function `checkTriplet` is used to check whether Pythagorean triplets exist in the array.
   - It finds the maximum element in the array and stores it in `MAX`.
   - It creates a frequency array `f` of size `MAX + 1` to count the frequency of elements in the input array.
   - It iterates through all pairs of elements `i` and `j` in the range `[1, MAX]` and calculates the square of their sum.
   - It uses the `findroot` function to find the square root of the sum.
   - If the square root is an integer (i.e., it's a perfect square) and it doesn't exceed `MAX`, the code continues.
   - It decreases the frequencies of elements `i`, `j`, and `k` (the square root) and checks if these frequencies are non-negative. If they are, it means that the Pythagorean triplet exists.
   - The code repeats this process for all pairs of elements.

3. **Return Result**: The code returns `1` if it finds a Pythagorean triplet, indicating "Yes." Otherwise, it returns `0`, indicating "No."

### Time and Space Complexity
- **Time Complexity**: O(n), where `n` is the size of the input array. The code iterates through all elements to build the frequency array and checks pairs of elements.
- **Space Complexity**: O(MAX), where `MAX` is the maximum element in the input array. The code uses a frequency array of size `MAX + 1`.

### Code (C++)
```cpp
class Solution{
public:
    int findroot(int n){
        int low = 1;
        int high = n;

        while(low < high - 1){
            int mid = low + (high - low) / 2;

            if(mid * mid > n)
                high = mid;
            else
                low = mid;
        }

        return low;
    }

    bool checkTriplet(int arr[], int n) {
        int MAX = *max_element(arr, arr + n);

        vector<int> f(MAX + 1, 0);

        for(int i = 0; i < n; i++)
            ++f[arr[i];

        for(int i = 1; i < MAX + 1; i++){
            for(int j = 1; j < MAX + 1; j++){
                int sq = i * i + j * i;
                int k = findroot(sq);

                if(k > MAX or k * k != sq)
                    continue;

                --f[i];
                --f[j];
                --f[k];

                if(f[i] >= 0 and f[j] >= 0 and f[k] >= 0){
                    return 1;
                }

                ++f[i];
                ++f[j];
                ++f[k];
            }
        }

        return 0;
    }
};
```

### Contribution and Support

For discussions, questions, or doubts related to this solution, please visit our [discussion section](https://github.com/iHRex/potd-gfg-leet/discussions). We welcome your input and aim to foster a collaborative learning environment.

If you find this solution helpful, consider supporting us by giving a ⭐ star to the [iHRex/potd-gfg-leet](https://github.com/iHRex/potd-gfg-leet) repository.