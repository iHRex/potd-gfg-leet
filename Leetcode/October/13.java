/*
746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.*/

class Solution {
    public int minCostClimbingStairs(int[] cost) {
    // Code here
        int n=cost.length;
        int[] dp=new int[n];
        dp[n-1]=cost[n-1];
        return Math.min(fun(0,cost,dp,n),fun(1,cost,dp,n));
    }
    int fun(int cur,int[] arr,int[] dp,int n){
        if(cur>=n) return 0;
        if(dp[cur]!=0) return dp[cur];
        return dp[cur]=arr[cur]+Math.min(fun(cur+1,arr,dp,n),fun(cur+2,arr,dp,n));    
    }
}