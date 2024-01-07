MAXINT = float('inf')

def reconstruct_partition(s, d, n, k):
    if k == 1:
        print_books(s, 1, n)
    else:
        reconstruct_partition(s, d, d[n][k], k - 1)
        print_books(s, d[n][k] + 1, n)


def print_books(s, start, end):
    sumc=0
    for i in range(start, end + 1):
        print(s[i], end=' ')
        sumc+=s[i]
    print("||no.of.pages= ",sumc)
    print()

def fair_partition(s, n, k, test_case):
    m = [[0] * (k + 1) for _ in range(n + 1)]  # DP table for values
    d = [[0] * (k + 1) for _ in range(n + 1)]  # DP table for dividers
    p = [0] * (n + 1)  # Prefix sums array

    # Construct prefix sums
    for i in range(1, n + 1):
        p[i] = p[i - 1] + s[i]

    # Initialize boundaries
    for i in range(1, n + 1):
        m[i][1] = p[i]

    for j in range(1, k + 1):
        m[1][j] = s[1]

    # Evaluate main recurrence
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            m[i][j] = MAXINT
            for x in range(1, i):
                cost = max(m[x][j - 1], p[i] - p[x])
                if m[i][j] > cost:
                    m[i][j] = cost
                    d[i][j] = x

    print(f"TestCase{test_case}:")
    print(f"Input: {s[1:n + 1]}")
    print()

    reconstruct_partition(s, d, n, k)  # Call the partition reconstruction function
    print("--------------------------------------")

# Get user input or load from test case files
user_choice = input("Enter '1' for user input OR \n'2' - load test cases from files: ")
print()

if user_choice == '1':
    arr = list(map(int, input("Enter space-separated integers for the array: ").split()))
    k_value = int(input("Enter the value of k: "))
    fair_partition(arr, len(arr) - 1, k_value, 1)
elif user_choice == '2':
    for i in range(1, 5):
        filename = f"testcase{i}.txt"
        with open(filename, 'r') as file:
            # Skip the first line (comment)
            file.readline()

            arr = list(map(int, file.readline().split()))
            k_value = int(file.readline())
            fair_partition(arr, len(arr) - 1, k_value, i)
else:
    print("Invalid choice. Exiting.")
