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

    def memo_util(i, j, memo):
        if i == j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        memo[i][j] = sys.maxsize

        for k in range(i, j):
            count = (
                memo_util(i, k, memo)
                + memo_util(k + 1, j, memo)
                + p[i - 1] * p[k] * p[j]
            )
            memo[i][j] = min(memo[i][j], count)

        return memo[i][j]

    return memo_util(1, n - 1, memo)

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
    recursive_calls = [0]
    memo_entries = [0]
    bottom_up_entries = [0]
    recursive_time = [0]
    memo_time = [0]
    bottom_up_time = [0]

    def analyze_recursive(p):
        start_time = timeit.default_timer()
        _ = matrix_rec(p, 1, len(p) - 1)
        recursive_time[0] = timeit.default_timer() - start_time
        recursive_calls[0] = count_recursive_calls(p)

    def analyze_memoization(p):
        start_time = timeit.default_timer()
        _ = matrix_memo(p)
        memo_time[0] = timeit.default_timer() - start_time
        memo_entries[0] = count_memo_entries(p)

    def analyze_bottom_up(p):
        start_time = timeit.default_timer()
        _ = matrix_dp(p)
        bottom_up_time[0] = timeit.default_timer() - start_time
        bottom_up_entries[0] = count_bottom_up_entries(p)

    analyze_recursive(p)
    analyze_memoization(p)
    analyze_bottom_up(p)

    return recursive_calls[0], memo_entries[0], bottom_up_entries[0], recursive_time[0], memo_time[0], bottom_up_time[0]

# Utility function to count memoization entries
def count_memo_entries(p):
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

# Utility function to count bottom-up entries
def count_bottom_up_entries(p):
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

# Utility function to count recursive calls
def count_recursive_calls(arr):
    count = [0]

    def matrix_rec(arr, i, j):
        count[0] += 1
        if i == j:
            return 0

        min_ops = sys.maxsize

        for k in range(i, j):
            result = (
                matrix_rec(arr, i, k)
                + matrix_rec(arr, k + 1, j)
                + arr[i - 1] * arr[k] * arr[j]
            )
            if result < min_ops:
                min_ops = result

        return min_ops

    _ = matrix_rec(arr, 1, len(arr) - 1)
    return count[0]

# Randomly generate large test cases
def generate_large_test_case(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Set the sizes for test cases
test_case_sizes = [2, 4, 6, 8, 10]

# Analyze test cases
for size in test_case_sizes:
    print(f"\nAnalyzing test case of size {size}:")
    test_case = generate_large_test_case(size)
    recursive_calls, memo_entries, bottom_up_entries, recursive_time, memo_time, bottom_up_time = analyze_performance(test_case)
    print(f"Recursive Calls: {recursive_calls}")
    print(f"Memoization Entries: {memo_entries}")
    print(f"Bottom-Up DP Entries: {bottom_up_entries}")
    print(f"Memoization vs. Bottom-Up Entries: {memo_entries} vs. {bottom_up_entries}")
    print(f"Recursive Time: {recursive_time:.6f} seconds")
    print(f"Memoization Time: {memo_time:.6f} seconds")
    print(f"Bottom-Up Time: {bottom_up_time:.6f} seconds")
