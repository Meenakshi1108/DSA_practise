import sys
import timeit
import random

# Matrix Chain Multiplication - Recursive Approach
def matrix_rec(arr, i, j):
    if i == j:
        return 0

    min_ops = sys.maxsize

    for k in range(i, j):
        count = (
            matrix_rec(arr, i, k)
            + matrix_rec(arr, k + 1, j)
            + arr[i - 1] * arr[k] * arr[j]
        )
        if count < min_ops:
            min_ops = count

    return min_ops

# Matrix Chain Multiplication - Memoization (Top-Down) Approach
def matrix_memo(p):
    n = len(p)
    memo = [[-1 for _ in range(n)] for _ in range(n)]

    def memo_util(i, j):
        if i == j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        memo[i][j] = sys.maxsize

        for k in range(i, j):
            count = (
                memo_util(i, k)
                + memo_util(k + 1, j)
                + p[i - 1] * p[k] * p[j]
            )
            memo[i][j] = min(memo[i][j], count)

        return memo[i][j]

    return memo_util(1, n - 1)

# Matrix Chain Multiplication - Bottom-Up Approach
def matrix_dp(p):
    n = len(p)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = sys.maxsize

            for k in range(i, j):
                count = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )
                dp[i][j] = min(dp[i][j], count)

    return dp[1][n - 1]

# Analyze performance
def analyze_performance(p):
    # Recursive Approach
    start_time = timeit.default_timer()
    _ = matrix_rec(p, 1, len(p) - 1)
    recursive_time = timeit.default_timer() - start_time

    # Memoization (Top-Down) Approach
    start_time = timeit.default_timer()
    _ = matrix_memo(p)
    memoization_time = timeit.default_timer() - start_time

    # Bottom-Up Approach
    start_time = timeit.default_timer()
    _ = matrix_dp(p)
    bottom_up_time = timeit.default_timer() - start_time

    return recursive_time, memoization_time, bottom_up_time

# Randomly generate large test cases
def generate_large_test_case(size):
    return [random.randint(1, 100) for _ in range(size)]

# Set the sizes for test cases
test_case_sizes = [10, 20, 30, 40, 50]

for size in test_case_sizes:
    print(f"\nAnalyzing test case of size {size}:")
    test_case = generate_large_test_case(size)

    recursive_time, memoization_time, bottom_up_time = analyze_performance(test_case)
    print(f"Recursive Time: {recursive_time:.6f} seconds")
    print(f"Memoization (Top-Down) Time: {memoization_time:.6f} seconds")
    print(f"Bottom-Up Time: {bottom_up_time:.6f} seconds")
