# Problem Statement: Min Cost Climbing Stairs

You are given an integer array `cost` where `cost[i]` represents the cost of the ith step on a staircase. When you pay the cost for a step, you can choose to climb either one or two steps. You can start from either the step with index 0 or the step with index 1. The goal is to find the minimum cost to reach the top of the staircase.

## Code Explanation

```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n];
        dp[n - 1] = cost[n - 1];
        return Math.min(fun(0, cost, dp, n), fun(1, cost, dp, n));
    }
    
    int fun(int cur, int[] arr, int[] dp, int n) {
        if (cur >= n) return 0;
        if (dp[cur] != 0) return dp[cur;
        return dp[cur] = arr[cur] + Math.min(fun(cur + 1, arr, dp, n), fun(cur + 2, arr, dp, n));
    }
}
```

### Brief Explanation

The `minCostClimbingStairs` method calculates the minimum cost to reach the top of the staircase. It uses dynamic programming to find the solution. 

- `n` is the length of the `cost` array, representing the number of steps in the staircase.
- An array `dp` is created to store the minimum cost at each step.
- `dp[n - 1]` is initialized with the cost of the last step (the top step).
- The method returns the minimum cost from either starting at step 0 or step 1.

The `fun` method is a recursive function that calculates the minimum cost to reach the top of the staircase:

- If the current step `cur` is greater than or equal to `n`, the cost is 0 (we have reached the top).
- If `dp[cur]` is not 0, it means we have already calculated the cost for this step, so we return the stored value.
- Otherwise, we calculate the cost for the current step as the cost of the step plus the minimum of the cost of the next step and the step after that.
- The `dp` array is updated with this calculated cost.

This code uses dynamic programming to efficiently find the minimum cost to climb the staircase by considering the minimum cost at each step and storing the results to avoid redundant calculations.

This explanation provides a brief overview of how the code works to solve the "Min Cost Climbing Stairs" problem.