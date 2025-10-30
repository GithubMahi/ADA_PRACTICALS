def matrix_chain_order(p):
n = len(p) - 1 # Number of matrices

# Create DP table m[i][j] for storing min multiplication cost
m = [[0 for _ in range(n)] for _ in range(n)]

# l is chain length
for l in range(2, n + 1): # l = 2 to n
for i in range(n - l + 1):
j = i + l - 1
m[i][j] = sys.maxsize # Initialize with infinity

for k in range(i, j):
# q = cost/scalar multiplications
q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
if q < m[i][j]:
    m[i][j] = q

return m[0][n - 1]

# Example dimensions: matrices A1:10x20, A2:20x30, A3:30x40
p = [10, 20, 30, 40]
min_cost = matrix_chain_order(p)
print("Minimum number of multiplications:", min_cost)
