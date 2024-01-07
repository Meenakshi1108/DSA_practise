import sys
import timeit
import random
import matplotlib.pyplot as plt
# Global variables to store recursive calls and entries in DP table
recursive_calls = 0
memo_entries = 0
bottom_up_entries = 0
memo = []

# 0/1 Knapsack Problem - Recursive Approach
def knapsack_rec(weights, values, capacity, n):
    global recursive_calls
    recursive_calls += 1

    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack_rec(weights, values, capacity, n - 1)
    else:
        without_item = knapsack_rec(weights, values, capacity, n - 1)
        with_item = values[n - 1] + knapsack_rec(weights, values, capacity - weights[n - 1], n - 1)
        return max(without_item, with_item)

# 0/1 Knapsack Problem - Memoization (Top-Down) Approach
def knapsack_memo(weights, values, capacity, n):
    global memo_entries, memo
    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    memo_entries += 1

    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_memo(weights, values, capacity, n - 1)
        return memo[n][capacity]
    else:
        without_item = knapsack_memo(weights, values, capacity, n - 1)
        with_item = values[n - 1] + knapsack_memo(weights, values, capacity - weights[n - 1], n - 1)
        memo[n][capacity] = max(without_item, with_item)
        return memo[n][capacity]

# 0/1 Knapsack Problem - Bottom-Up Approach
def knapsack_dp(weights, values, capacity, n):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
                global bottom_up_entries
                bottom_up_entries += 1
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Analyze performance
def analyze_performance(weights, values, capacity):
    global recursive_calls, memo_entries, bottom_up_entries, memo

    # Reset global variables
    recursive_calls = 0
    memo_entries = 0
    bottom_up_entries = 0
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    # Recursive Approach
    start_time = timeit.default_timer()
    _ = knapsack_rec(weights, values, capacity, len(weights))
    recursive_time = timeit.default_timer() - start_time

    # Memoization (Top-Down) Approach
    start_time = timeit.default_timer()
    _ = knapsack_memo(weights, values, capacity, len(weights))
    memoization_time = timeit.default_timer() - start_time

    # Bottom-Up Approach
    start_time = timeit.default_timer()
    _ = knapsack_dp(weights, values, capacity, len(weights))
    bottom_up_time = timeit.default_timer() - start_time

    return recursive_calls, memo_entries, bottom_up_entries, recursive_time, memoization_time, bottom_up_time

# Randomly generate weights and values for the knapsack problem
def generate_random_knapsack_instance(size, max_weight, max_value):
    weights = [random.randint(1, max_weight) for _ in range(size)]
    values = [random.randint(1, max_value) for _ in range(size)]
    return weights, values

# Analyze knapsack test cases and collect data for plotting
sizes = []
recursive_times = []
memoization_times = []
bottom_up_times = []

for size in range(1, 25):  # Analyzing for a range of sizes
    weights, values = generate_random_knapsack_instance(size, 100, 1000)
    capacity = 2000
    # Analyzing each method's performance for the same set of weights, values, and capacity
    recursive_calls, memo_entries, bottom_up_entries, recursive_time, memo_time, bottom_up_time = analyze_performance(weights, values, capacity)

    sizes.append(size)
    recursive_times.append(recursive_time)
    memoization_times.append(memo_time)
    bottom_up_times.append(bottom_up_time)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, recursive_times, marker='o', label='Recursive Time')
plt.plot(sizes, memoization_times, marker='o', label='Memoization (Top-Down) Time')
plt.plot(sizes, bottom_up_times, marker='o', label='Bottom-Up Time')

plt.title('0/1 Knapsack Problem - Performance Comparison')
plt.xlabel('Test Case Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()