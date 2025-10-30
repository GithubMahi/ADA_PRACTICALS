def fractional_knapsack(value, weight, capacity):
n = len(value)
ratio = [(value[i]/weight[i], value[i], weight[i]) for i in range(n)]
ratio.sort(reverse=True) # sort by value/weight ratio

total_value = 0
for r, v, w in ratio:
if capacity >= w:
total_value += v
capacity -= w
else:
total_value += r * capacity
break

return total_value

# Example 
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(value, weight, capacity)
print("Maximum value (Fractional Knapsack):", max_value)
