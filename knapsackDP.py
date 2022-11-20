# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP
 
# driver code
val = [60, 100, 120 ]
wt = [10, 20, 30 ]
W = 50
n = len(val)
 
# We initialize the matrix with -1 at first.
dp = [[-1 for i in range(W + 1)] for j in range(n + 1)]
 
 
def knapsack(wt, val, W, n):
 
    # base conditions
    if n == 0 or W == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
 
    # choice diagram code
    if wt[n-1] <= W:
        dp[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1),
        knapsack(wt, val, W, n-1))
        return dp[n][W]
    elif wt[n-1] > W:
        dp[n][W] = knapsack(wt, val, W, n-1)
        return dp[n][W]
print(knapsack(wt, val, W, n))