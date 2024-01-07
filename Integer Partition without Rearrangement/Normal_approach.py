def can_partition(arr, k, max_sum):
    partitions = 0
    current_sum = 0
    
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            partitions += 1
            current_sum = num
    
    partitions += 1  # Count the last partition
    
    return partitions <= k

def print_partitions(arr, max_sum):
    current_sum = 0
    partitions = []
    largest_job = 0
    smallest_job = float('inf')

    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            partitions.append('|')
            largest_job = max(largest_job, current_sum - num)
            smallest_job = min(smallest_job, current_sum - num)
            current_sum = num
        partitions.append(num)

    largest_job = max(largest_job, current_sum)
    smallest_job = min(smallest_job, current_sum)
    
    print(" ".join(map(str, partitions)))
    print("Largest Job:", largest_job)
    print("Smallest Job:", smallest_job)

def fair_partition(arr, k_values, testcase_number):
    if not arr:
        print(f"Test Case {testcase_number}: Array is empty.")
        return
    
    for k in k_values:
        low, high = min(arr), sum(arr)
        
        while low < high:
            mid = (low + high) // 2
            if can_partition(arr, k, mid):
                high = mid
            else:
                low = mid + 1
        
        print(f"\nTestCase{testcase_number} -For k={k}:")
        print("Input:", arr)
        print()
        print_partitions(arr, low)
        print("------------------------------")

# Get user input or load from test case files
user_choice = input("Enter '1' for user input OR \n'2'- load testcases from files: ")
print()

if user_choice == '1':
    arr = list(map(int, input("Enter space-separated integers for the array: ").split()))
    k_values = list(map(int, input("Enter space-separated integers for k values: ").split()))
    fair_partition(arr, k_values, 1)
elif user_choice == '2':
    for i in range(1, 5):
        filename = f"testcase{i}.txt"
        with open(filename, 'r') as file:
            # Skip the first line (comment)
            file.readline()
            
            arr = list(map(int, file.readline().split()))
            k_values = list(map(int, file.readline().split()))
            fair_partition(arr, k_values, i)
else:
    print("Invalid choice. Exiting.")
