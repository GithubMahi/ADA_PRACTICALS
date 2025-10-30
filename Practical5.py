def knapsack(values, weights, capacity):
n = len(values)

# Create a 2D DP table of size (n+1) x (capacity+1)
dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

# Build the table in bottom-up manner
for i in range(1, n + 1):
for w in range(1, capacity + 1):
if weights[i - 1] <= w:
# Include the item or exclude it — take max
dp[i][w] = max(
values[i - 1] + dp[i - 1][w - weights[i - 1]],
dp[i - 1][w]
)
else:
    dp[i][w] = dp[i - 1][w]

return dp[n][capacity]

# Example input
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# Call function
max_value = knapsack(values, weights, capacity)
